from bs4 import BeautifulSoup as bs
import utils.emtinfo as emtinfo


# Create 'sopup' object
def soup_html(numParada, numLinea=''):
    # Get raw info from emt web
    raw_data = emtinfo.get_info(numParada, numLinea)
    soup = bs(raw_data.text, "html.parser")
    return soup


# Parsing to get next buses
def next_buses(numParada, numLinea=''):
    # Get soup object
    data = soup_html(numParada, numLinea)
    # Debug vars
    # spans = data.select('span')
    # # span with line img
    # span_linea = data.find_all('span', {'class': 'imagenParada'})
    # line and time remaining span
    spanTimeRemain = data.find_all('span', {'class': 'llegadaHome'})
    # img containing line
    imgElem = data.select('img')
    buses = ''
    linea = ''
    # Loop showing line and time remaining
    for span, img in zip(spanTimeRemain, imgElem):
        linea = img.get('title')
        show = span.getText(strip=True)
        linea = str(linea)
        show = str(show)
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
