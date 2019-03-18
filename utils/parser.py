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


def error_output(inMsg):
    error_msg = {
        'SIN ESTIMACIONES': 'Sin estimaciones. ¿Seguro que esta linea pasa por esta parada?',
        'PARADA NO CORRESPONDE': 'La linea no corresponde con esta parada',
        'Temporalmente no disponible. Actualiza la estimación en unos segundos.': 'La parada no existe o esta temporalmente no disponible'
    }
    output = error_msg.get(inMsg, "ERROR")
    return output


# Generate msg with parsed info or errors
def generate_msg(info):
    output = ''
    # Check if no data
    if info[0][0] is None:
        # Get error_msg
        output = error_output(info[0][1])
    else:
        for row in info:
            output += (' '.join([str(elem) for elem in row]) + '\n')
    return output


def next_buses(numParada, numLinea=''):
    soup_obj = generate_soup(numParada, numLinea)
    info = parse_soup(soup_obj)
    return generate_msg(info)
