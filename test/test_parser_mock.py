from unittest import TestCase
from utils.parser import next_buses
import responses


class TestParserMock(TestCase):
    @responses.activate
    def test_sin_estimaciones(self):
        fake_data = \
            '<img align="left" src="modules/mod_tiempo/img/icono peligro.jpg"/><span class="llegadaHome">SIN ESTIMACIONES</span>'
        responses.add(responses.POST, 'http://movil.emtvalencia.es/mod_tiempo/busca_parada.php',
                      body=fake_data, status=200,
                      content_type='application/x-www-form-urlencoded')
        info = next_buses("19321")
        expected = 'Sin estimaciones. ¿Seguro que esta linea pasa por esta parada?'
        self.assertEqual(expected, info)

    @responses.activate
    def test_next_buses(self):
        fake_data = \
            '<span class="imagenParada"><img height="25px" src="http://www.emtvalencia.es/EmtEsquemas_graphics/line-icons/9bigW.gif" title="9" width="25px"/></span>, <img height="25px" src="http://www.emtvalencia.es/EmtEsquemas_graphics/line-icons/9bigW.gif" title="9" width="25px"/>, <span class="llegadaHome">  Pl. Espanya - 6 min.</span>, <br/>, <span class="imagenParada"><img height="25px" src="http://www.emtvalencia.es/EmtEsquemas_graphics/line-icons/9bigW.gif" title="9" width="25px"/></span>, <img height="25px" src="http://www.emtvalencia.es/EmtEsquemas_graphics/line-icons/9bigW.gif" title="9" width="25px"/>, <span class="llegadaHome">  Pl. Espanya - 10 min.</span>, <br/>'
        responses.add(responses.POST, 'http://movil.emtvalencia.es/mod_tiempo/busca_parada.php',
                      body=fake_data, status=200,
                      content_type='application/x-www-form-urlencoded')
        info = next_buses("1932", "9")
        expected = '9 Pl. Espanya - 6 min.\n9 Pl. Espanya - 10 min.\n'
        self.assertEqual(expected, info)
