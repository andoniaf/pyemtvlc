from bs4 import BeautifulSoup as bs
import utils.emtinfo as emtinfo


# Create 'soup' object
def generate_soup(numParada, numLinea=''):
    # Get raw info from emt web
    raw_data = emtinfo.get_info(numParada, numLinea)
    soup = bs(raw_data.text, "html.parser")
    return soup


# Parse soup object to extract info
def parse_soup(soup):
    # data is inside spans
    spanTimeData = soup.find_all('span', {'class': 'llegadaHome'})
    # img tag contain line num
    imgElem = soup.select('img')
    info = []
    for span, img in zip(spanTimeData, imgElem):
        linea = img.get('title')
        time = span.getText(strip=True)
        busTime = [linea, time]
        info.append(busTime)
    return info


# Manage info
def next_buses(info):
    buses = ''
    firstKey = next(iter(info[0]))
    if str(firstKey) == 'None':
        #Check el values para la excep
    if info[0] == {None: 'SIN ESTIMACIONES'}:
        buses = "Sin estimaciones. ¿Pasa esta linea por esta parada?"
    elif info[0] == {None: 'Temporalmente no disponible. Actualiza la estimación en unos segundos.'}:
        buses = "Sin estimaciones. ¿Pasa esta linea por esta parada?"
    else:
        for bus in info:
            buses += str(bus) + "\n"
    return buses

    # Loop showing line and time remaining
    for span, img in zip(spanTimeData, imgElem):
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
