import xml.etree.ElementTree as ET
from unittest import TestCase
from utils.parser import generate_msg, parse_xml


class TestParser(TestCase):
    def test_msg_generator(self):
        info = [['9', 'Pl. Espanya - 3 min.'], ['10', 'Benimaclet - 4 min.']]
        msg = generate_msg(info)
        expected = '9 Pl. Espanya - 3 min.\n10 Benimaclet - 4 min.\n'
        self.assertEqual(expected, msg)

    def test_error_sinestimaciones(self):
        info = [[None, 'SIN ESTIMACIONES']]
        msg = generate_msg(info)
        expected = 'Sin estimaciones. ¿Seguro que esta linea pasa por esta parada?'
        self.assertEqual(expected, msg)

    def test_xml_parse(self):
        fake_xml = """<?xml version='1.0' encoding='UTF-8'?>
<estimacion parada="636">
  <solo_parada>
    <bus>
      <linea>9</linea>
      <destino>Pl. Espanya</destino>
      <minutos>6 min.</minutos>
      <horaLlegada/>
      <error/>
    </bus>
    <bus>
      <linea>9</linea>
      <destino>Pl. Espanya</destino>
      <minutos>10 min.</minutos>
      <horaLlegada/>
      <error/>
    </bus>
  </solo_parada>
  <parada_linea/>
  <info/>
</estimacion>"""
        root = ET.fromstring(fake_xml)
        info = parse_xml(root)
        expected = [['9', 'Pl. Espanya - 6 min.'], ['9', 'Pl. Espanya - 10 min.']]
        self.assertEqual(expected, info)

    def test_xml_parse_horallegada(self):
        fake_xml = """<?xml version='1.0' encoding='UTF-8'?>
<estimacion parada="636">
  <solo_parada>
    <bus>
      <linea>N7</linea>
      <destino>Pl. Ajuntament</destino>
      <minutos/>
      <horaLlegada>22:38</horaLlegada>
      <error/>
    </bus>
  </solo_parada>
  <parada_linea/>
  <info/>
</estimacion>"""
        root = ET.fromstring(fake_xml)
        info = parse_xml(root)
        expected = [['N7', 'Pl. Ajuntament - 22:38']]
        self.assertEqual(expected, info)
