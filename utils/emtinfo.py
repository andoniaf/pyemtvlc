import requests

EMT_URL = 'https://geoportal.emtvalencia.es/EMT/mapfunctions/MapUtilsPetitions.php'

_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://geoportal.emtvalencia.es/visor?lang=es',
    'Connection': 'keep-alive',
}


def get_info(numParada, numLinea=''):
    params = {
        'sec': 'getSAE',
        'parada': numParada,
        'adaptados': 'false',
        'idioma': 'es',
    }
    if numLinea:
        params['linea'] = numLinea
    res = requests.get(EMT_URL, headers=_headers, params=params)
    return res
