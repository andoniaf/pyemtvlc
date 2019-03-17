from bs4 import BeautifulSoup as bs
import utils.emtinfo as info


# Create 'sopup' object
def soup_html(numParada):
    # Get raw info from emt web
    raw_data = info.get_parada(numParada)
    soup = bs(raw_data, "html.parser")
    return soup


# Parsing to get next buses
def next_buses(numParada):
    # Get soup object
    data = soup_html(numParada)
    # Debug vars
    # spans = data.select('span')
    # # span with line img
    # span_linea = data.find_all('span', {'class': 'imagenParada'})
    # line and time remaining span
    span_tiempos = data.find_all('span', {'class': 'llegadaHome'})
    # img containing line
    imgElem = data.select('img')
    buses = ''
    linea = ''
    # Loop showing line and time remaining
    for span, img in zip(span_tiempos, imgElem):
        linea = img.get('title')
        show = span.getText(strip=True)
        # show = show.encode('utf-8')
        linea = str(linea)
        show = str(show)
        # print(linea, show)
        buses += linea + ': ' + show + "\n"
    if buses == 'None: PARADA NO CORRESPONDE\n':
        buses = "La linea " + numLinea + " no pasa por esta parada."
        return buses
    elif buses == 'None: LINEA NO ENCONTRADA\n':
        buses = "Todavia no hay estimaciones para la linea " + numLinea
        buses += " en esta parada."
        return buses
    if linea == 'None':
        buses = "Temporalmente fuera de servicio."
    if buses == '':
        buses += "No quedan buses... O la parada introducida no existe."
    return buses
