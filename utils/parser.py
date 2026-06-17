import xml.etree.ElementTree as ET
import utils.emtinfo as emtinfo


def get_xml(numParada, numLinea=''):
    raw_data = emtinfo.get_info(numParada, numLinea)
    return ET.fromstring(raw_data.text)


def parse_xml(root):
    # root tag is <estimacion>, buses are inside <solo_parada> or <parada_linea>
    container = root.find('solo_parada')
    if container is None:
        container = root.find('parada_linea')
    if container is None:
        return [[None, '']]

    buses = container.findall('bus')
    if not buses:
        return [[None, '']]

    info = []
    for bus in buses:
        linea = bus.findtext('linea', '').strip()
        destino = bus.findtext('destino', '').strip()
        minutos = bus.findtext('minutos', '').strip()
        hora = bus.findtext('horaLlegada', '').strip()
        error = bus.findtext('error', '').strip()

        if error:
            info.append([None, error])
            continue

        time = hora if not minutos else minutos
        info.append([linea, destino + ' - ' + time])

    return info if info else [[None, '']]


def error_output(inMsg):
    error_msg = {
        'SIN ESTIMACIONES': 'Sin estimaciones. ¿Seguro que esta linea pasa por esta parada?',
        'PARADA NO CORRESPONDE': 'La linea no corresponde con esta parada',
        'Temporalmente no disponible. Actualiza la estimación en unos segundos.': 'La parada no existe o esta temporalmente no disponible',
        '': 'La parada no existe o esta temporalmente no disponible'
    }
    return error_msg.get(inMsg, "ERROR")


def generate_msg(info):
    output = ''
    if info[0][0] is None:
        output = error_output(info[0][1])
    else:
        for row in info:
            output += (' '.join([str(elem) for elem in row]) + '\n')
    return output


def next_buses(numParada, numLinea=''):
    root = get_xml(numParada, numLinea.upper())
    info = parse_xml(root)
    return generate_msg(info)
