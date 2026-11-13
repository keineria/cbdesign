<?php
/**
 * Buscador de dominios de CBdesign.
 *
 * GET /api/dominios.php?q=mimarca[&tld=com]
 * Responde JSON: { "name": "mimarca", "results": [ { "domain", "tld", "status", "via" } ] }
 * status: available | taken | likely | unknown
 *   likely = el registro no respondió, pero el dominio no existe en el DNS (casi seguro libre).
 *
 * Consulta la disponibilidad real en este orden:
 *   1. RDAP del registro oficial de cada extensión (en paralelo).
 *   2. WHOIS (puerto 43) si la extensión no tiene RDAP (.co, .com.co, .io) o no responde.
 *      El servidor debe permitir conexiones salientes al puerto 43.
 *   3. DNS: con servidores de nombres está registrado; sin ellos, probablemente libre.
 * No requiere cuentas ni llaves de terceros. Requiere PHP 7.4+ con cURL.
 */
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
header('X-Robots-Tag: noindex, nofollow');
header('X-Content-Type-Options: nosniff');

const TLDS = ['com', 'co', 'com.co', 'net', 'org', 'store', 'online', 'app', 'io', 'dev'];

/* Servidores RDAP conocidos. Se completan con el directorio oficial de IANA (en caché). */
const RDAP_FIJO = [
    'com' => 'https://rdap.verisign.com/com/v1/',
    'net' => 'https://rdap.verisign.com/net/v1/',
    'org' => 'https://rdap.publicinterestregistry.org/rdap/',
];
/* Servidores WHOIS conocidos. Los demás se averiguan en whois.iana.org (en caché). */
const WHOIS_FIJO = [
    'com' => 'whois.verisign-grs.com',
    'net' => 'whois.verisign-grs.com',
    'org' => 'whois.publicinterestregistry.org',
    'io'  => 'whois.nic.io',
];
/* Se usan solo si whois.iana.org no responde. */
const WHOIS_RESPALDO = [
    'co' => 'whois.registry.co',
];
const LIMITE_POR_MINUTO = 20;
const CACHE_OCUPADO = 900;   // segundos
const CACHE_LIBRE   = 120;
const DIR_CACHE     = 'cbdesign-dominios';

function responder(int $codigo, array $datos): void
{
    http_response_code($codigo);
    echo json_encode($datos, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    exit;
}

function dir_cache(): string
{
    $d = rtrim(sys_get_temp_dir(), '/') . '/' . DIR_CACHE;
    if (!is_dir($d)) {
        @mkdir($d, 0700, true);
    }
    return $d;
}

function cache_leer(string $clave, int $vida)
{
    $f = dir_cache() . '/' . sha1($clave) . '.json';
    if (is_file($f) && (time() - (int) @filemtime($f)) < $vida) {
        $v = json_decode((string) @file_get_contents($f), true);
        return $v === null ? false : $v;
    }
    return false;
}

function cache_guardar(string $clave, $valor): void
{
    @file_put_contents(dir_cache() . '/' . sha1($clave) . '.json', json_encode($valor), LOCK_EX);
}

/** Límite simple por IP para que nadie use el buscador como servicio masivo. */
function limite_ok(): bool
{
    $ip = $_SERVER['REMOTE_ADDR'] ?? '0';
    $f = dir_cache() . '/ip-' . sha1($ip) . '.json';
    $ahora = time();
    $h = @fopen($f, 'c+');
    if (!$h) {
        return true;
    }
    flock($h, LOCK_EX);
    $marcas = json_decode((string) stream_get_contents($h), true);
    $marcas = is_array($marcas) ? array_values(array_filter($marcas, fn($t) => $t > $ahora - 60)) : [];
    $ok = count($marcas) < LIMITE_POR_MINUTO;
    if ($ok) {
        $marcas[] = $ahora;
    }
    ftruncate($h, 0);
    rewind($h);
    fwrite($h, json_encode($marcas));
    flock($h, LOCK_UN);
    fclose($h);
    return $ok;
}

function limpiar_nombre(string $q): string
{
    $q = strtolower(trim($q));
    $q = strtr($q, ['á' => 'a', 'é' => 'e', 'í' => 'i', 'ó' => 'o', 'ú' => 'u', 'ü' => 'u', 'ñ' => 'n',
                    'Á' => 'a', 'É' => 'e', 'Í' => 'i', 'Ó' => 'o', 'Ú' => 'u', 'Ü' => 'u', 'Ñ' => 'n']);
    $q = preg_replace('~^[a-z]+://~', '', $q);
    $q = preg_replace('~^www\.~', '', $q);
    $q = preg_replace('~[/?#].*$~', '', $q);
    $q = preg_replace('~\s+~', '', $q);
    $p = strpos($q, '.');
    if ($p !== false) {
        $q = substr($q, 0, $p);
    }
    return trim((string) preg_replace('~[^a-z0-9-]~', '', $q), '-');
}

/** Extensión de primer nivel: "com.co" pertenece al registro de "co". */
function tld_raiz(string $tld): string
{
    $p = strrpos($tld, '.');
    return $p === false ? $tld : substr($tld, $p + 1);
}

/** Directorio oficial RDAP de IANA, guardado 7 días. */
function rdap_directorio(): array
{
    $mapa = cache_leer('rdap-iana', 7 * 86400);
    if (is_array($mapa)) {
        return $mapa;
    }
    $mapa = [];
    $c = curl_init('https://data.iana.org/rdap/dns.json');
    curl_setopt_array($c, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 6, CURLOPT_CONNECTTIMEOUT => 4, CURLOPT_FOLLOWLOCATION => true]);
    $json = json_decode((string) curl_exec($c), true);
    curl_close($c);
    foreach (($json['services'] ?? []) as $servicio) {
        $url = $servicio[1][0] ?? null;
        if (!$url) {
            continue;
        }
        foreach ($servicio[0] as $t) {
            $mapa[strtolower($t)] = rtrim($url, '/') . '/';
        }
    }
    if ($mapa) {
        cache_guardar('rdap-iana', $mapa);
    }
    return $mapa;
}

/** Consulta RDAP en paralelo. Devuelve [dominio => 'taken' | 'available' | null]. */
function rdap_consultar(array $dominios): array
{
    $dir = null;
    $mh = curl_multi_init();
    $hs = [];
    $res = [];
    foreach ($dominios as $dominio => $tld) {
        $res[$dominio] = null;
        $raiz = tld_raiz($tld);
        $base = RDAP_FIJO[$raiz] ?? null;
        if (!$base) {
            $dir = $dir ?? rdap_directorio();
            $base = $dir[$raiz] ?? null;
        }
        if (!$base) {
            continue;
        }
        $c = curl_init($base . 'domain/' . $dominio);
        curl_setopt_array($c, [
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_TIMEOUT => 7,
            CURLOPT_CONNECTTIMEOUT => 4,
            CURLOPT_FOLLOWLOCATION => true,
            CURLOPT_MAXREDIRS => 3,
            CURLOPT_HTTPHEADER => ['Accept: application/rdap+json'],
            CURLOPT_USERAGENT => 'CBdesign-buscador-dominios/1.0',
        ]);
        curl_multi_add_handle($mh, $c);
        $hs[$dominio] = $c;
    }
    do {
        $estado = curl_multi_exec($mh, $activos);
        if ($activos) {
            curl_multi_select($mh, 1.0);
        }
    } while ($activos && $estado === CURLM_OK);
    foreach ($hs as $dominio => $c) {
        $http = (int) curl_getinfo($c, CURLINFO_HTTP_CODE);
        $cuerpo = (string) curl_multi_getcontent($c);
        if ($http === 404) {
            $res[$dominio] = 'available';
        } elseif ($http === 200 && strpos($cuerpo, 'objectClassName') !== false) {
            $res[$dominio] = 'taken';
        }
        curl_multi_remove_handle($mh, $c);
        curl_close($c);
    }
    curl_multi_close($mh);
    return $res;
}

function whois_enviar(string $servidor, string $consulta, int $espera = 5): string
{
    $s = @fsockopen($servidor, 43, $errno, $errstr, $espera);
    if (!$s) {
        return '';
    }
    stream_set_timeout($s, $espera);
    fwrite($s, $consulta . "\r\n");
    $txt = '';
    while (!feof($s) && strlen($txt) < 20000) {
        $parte = fread($s, 4096);
        if ($parte === false || $parte === '') {
            if (stream_get_meta_data($s)['timed_out']) {
                break;
            }
            continue;
        }
        $txt .= $parte;
    }
    fclose($s);
    return $txt;
}

function whois_servidor(string $raiz): ?string
{
    if (isset(WHOIS_FIJO[$raiz])) {
        return WHOIS_FIJO[$raiz];
    }
    $c = cache_leer('whois-srv-' . $raiz, 30 * 86400);
    if (is_string($c)) {
        return $c ?: null;
    }
    $txt = whois_enviar('whois.iana.org', $raiz);
    $srv = preg_match('~^whois:\s*(\S+)~mi', $txt, $m) ? strtolower($m[1]) : '';
    if ($txt !== '') {
        cache_guardar('whois-srv-' . $raiz, $srv);
    }
    return $srv ?: (WHOIS_RESPALDO[$raiz] ?? null);
}

function whois_consultar(string $dominio, string $tld): ?string
{
    $srv = whois_servidor(tld_raiz($tld));
    if (!$srv) {
        return null;
    }
    $txt = whois_enviar($srv, $dominio);
    if ($txt === '') {
        return null;
    }
    if (preg_match('~no match for|not found|no data found|no entries found|no object found|domain not found|is available|status:\s*(free|available)|^available~mi', $txt)) {
        return 'available';
    }
    if (preg_match('~domain name:\s*\S+|registrar:|creation date:|registry domain id:~i', $txt)) {
        return 'taken';
    }
    return null;
}

/** DNS: 'taken' si tiene servidores de nombres, 'likely' si no existe, null si no se pudo consultar. */
function dns_estado(string $dominio): ?string
{
    if (!function_exists('dns_get_record')) {
        return null;
    }
    $ns = @dns_get_record($dominio . '.', DNS_NS);
    if ($ns) {
        return 'taken';
    }
    /* Una respuesta vacía solo significa "no existe" si el DNS de este servidor funciona:
       se comprueba resolviendo la propia extensión (.co, .io...), que siempre tiene servidores. */
    static $dns_ok = [];
    $raiz = tld_raiz(substr($dominio, strpos($dominio, '.') + 1));
    if (!isset($dns_ok[$raiz])) {
        $dns_ok[$raiz] = (bool) @dns_get_record($raiz . '.', DNS_NS);
    }
    return ($ns !== false && $dns_ok[$raiz]) ? 'likely' : null;
}

/* ------------------------------------------------------------------ */

if (($_SERVER['REQUEST_METHOD'] ?? 'GET') !== 'GET') {
    header('Allow: GET');
    responder(405, ['error' => 'method']);
}
if (!function_exists('curl_init')) {
    responder(500, ['error' => 'curl']);
}

$nombre = limpiar_nombre((string) ($_GET['q'] ?? ''));
if (!preg_match('~^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$~', $nombre) || strlen($nombre) < 2) {
    responder(400, ['error' => 'invalid', 'message' => 'Nombre de dominio no válido.']);
}
if (!limite_ok()) {
    header('Retry-After: 60');
    responder(429, ['error' => 'rate', 'message' => 'Demasiadas consultas. Intenta de nuevo en un minuto.']);
}

$orden = TLDS;
$primero = strtolower((string) ($_GET['tld'] ?? ''));
if (in_array($primero, TLDS, true)) {
    $orden = array_merge([$primero], array_values(array_diff(TLDS, [$primero])));
}

$resultados = [];
$pendientes = [];
foreach ($orden as $tld) {
    $dominio = $nombre . '.' . $tld;
    $c = cache_leer('d-' . $dominio, CACHE_OCUPADO);
    $f = dir_cache() . '/' . sha1('d-' . $dominio) . '.json';
    if (is_array($c) && ($c['status'] === 'taken' || (time() - (int) @filemtime($f)) < CACHE_LIBRE)) {
        $resultados[$dominio] = ['domain' => $dominio, 'tld' => $tld, 'status' => $c['status'], 'via' => $c['via']];
    } else {
        $resultados[$dominio] = null;
        $pendientes[$dominio] = $tld;
    }
}

if ($pendientes) {
    $rdap = rdap_consultar($pendientes);
    foreach ($pendientes as $dominio => $tld) {
        $estado = $rdap[$dominio];
        $via = 'rdap';
        if ($estado === null) {
            $estado = whois_consultar($dominio, $tld);
            $via = 'whois';
        }
        if ($estado === null) {
            /* Sin respuesta del registro: el DNS confirma si está ocupado o sugiere que está libre. */
            $estado = dns_estado($dominio) ?? 'unknown';
            $via = 'dns';
        }
        $resultados[$dominio] = ['domain' => $dominio, 'tld' => $tld, 'status' => $estado, 'via' => $via];
        if ($estado === 'taken' || $estado === 'available') {
            cache_guardar('d-' . $dominio, ['status' => $estado, 'via' => $via]);
        }
    }
}

responder(200, ['name' => $nombre, 'results' => array_values($resultados)]);
