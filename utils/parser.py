from bs4 import BeautifulSoup as bs
import utils.emtinfo as info


# Create 'sopup' object
def soup_html(numParada):
    # Datos que provienen de la funcion get_parada
    raw_data = info.get_parada(numParada)
    soup = bs(raw_data, "html.parser")
    return soup


# Parsing to get next buses
def prime_buses(numParada):
    # Objeto que proviene de la funcion soup_html
    data = soup_html(numParada)
    # Todos los span
    # spans = data.select('span')
    # Los span con la imagen de la linea
    # span_linea = data.find_all('span', {'class': 'imagenParada'})
    # Los span con el nombre de la linea y el tiempo
    span_tiempos = data.find_all('span', {'class': 'llegadaHome'})
    # Los img donde aparece la linea
    imgElem = data.select('img')
    buses = ''
    linea = ''
    # Bucle para mostrar linea y tiempo
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
        buses = "Todavia no hay estimaciones para la linea " + numLinea + " en esta parada."
        return buses
    if linea == 'None':
        buses = "Temporalmente fuera de servicio."
    if buses == '':
        buses += "No quedan buses... O la parada introducida no existe."
    return buses
