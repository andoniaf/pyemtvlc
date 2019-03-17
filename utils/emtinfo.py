import requests


def get_info(numParada, numLinea=''):
    cookies = {
        '__utma': '25540009.1894639261.1539253515.1550245270.1552753595.4',
        '__utmz': '25540009.1552753595.4.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
        '__utmb': '25540009.4.10.1552753595',
        '__utmc': '25540009',
        'PHPSESSID': 'aj1va5hon0r7uuhiqehrogco96',
        'nombreparada': numParada,
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Accept': '*/*',
        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer': 'http://movil.emtvalencia.es/index.php?op=pl',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
    data = {
        'parada': numParada,
        'adaptados': '0',
        'usuario': 'movilemt',
        'linea': numLinea,
        'idioma': 'es'
    }
    emt_url = 'http://movil.emtvalencia.es/mod_tiempo/busca_parada.php'
    res = requests.post(emt_url, headers=headers, cookies=cookies, data=data)
    return res
