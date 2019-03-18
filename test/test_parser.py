from unittest import TestCase
from utils.parser import generate_msg, parse_soup
from bs4 import BeautifulSoup as bs


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

    def test_soup_parse(self):
        fake_res = \
            '[<span class="imagenParada"><img height="25px" src="http://www.emtvalencia.es/EmtEsquemas_graphics/line-icons/9bigW.gif" title="9" width="25px"/></span>, <img height="25px" src="http://www.emtvalencia.es/EmtEsquemas_graphics/line-icons/9bigW.gif" title="9" width="25px"/>, <span class="llegadaHome">  Pl. Espanya - 6 min.</span>, <br/>, <span class="imagenParada"><img height="25px" src="http://www.emtvalencia.es/EmtEsquemas_graphics/line-icons/9bigW.gif" title="9" width="25px"/></span>, <img height="25px" src="http://www.emtvalencia.es/EmtEsquemas_graphics/line-icons/9bigW.gif" title="9" width="25px"/>, <span class="llegadaHome">  Pl. Espanya - 10 min.</span>, <br/>]'
        soup = bs(fake_res, "html.parser")
        info = parse_soup(soup)
        expected = [['9', 'Pl. Espanya - 6 min.'], ['9', 'Pl. Espanya - 10 min.']]
        self.assertEqual(expected, info)
