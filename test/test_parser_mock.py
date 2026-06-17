from unittest import TestCase
from utils.parser import next_buses
import responses
from utils.emtinfo import EMT_URL


class TestParserMock(TestCase):
    @responses.activate
    def test_sin_estimaciones(self):
        fake_data = """<?xml version='1.0' encoding='UTF-8'?>
<estimacion parada="19321">
  <solo_parada>
    <bus>
      <linea>9</linea>
      <destino>Pl. Espanya</destino>
      <minutos/>
      <horaLlegada/>
      <error>SIN ESTIMACIONES</error>
    </bus>
  </solo_parada>
  <parada_linea/>
  <info/>
</estimacion>"""
        responses.add(responses.GET, EMT_URL, body=fake_data, status=200)
        info = next_buses("19321")
        expected = 'Sin estimaciones. ¿Seguro que esta linea pasa por esta parada?'
        self.assertEqual(expected, info)

    @responses.activate
    def test_next_buses(self):
        fake_data = """<?xml version='1.0' encoding='UTF-8'?>
<estimacion parada="1932">
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
        responses.add(responses.GET, EMT_URL, body=fake_data, status=200)
        info = next_buses("1932", "9")
        expected = '9 Pl. Espanya - 6 min.\n9 Pl. Espanya - 10 min.\n'
        self.assertEqual(expected, info)
