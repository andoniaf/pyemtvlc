from subprocess import PIPE, Popen as popen
from unittest import TestCase


class BasicOutputs(TestCase):
    def test_returns_usage_information(self):
        output = str(popen(['pyemtvlc'], stdout=PIPE).communicate()[0])
        self.assertTrue('Uso:' in output)

    def test_returns_parada_echo(self):
        output = str(popen(['pyemtvlc', '13'], stdout=PIPE).communicate()[0])
        self.assertTrue('Parada: 13' in output)

    def test_returns_unvalid_parada_echo(self):
        output = str(popen(['pyemtvlc', 'abcd'], stdout=PIPE).communicate()[0])
        self.assertTrue('No has introducido un' in output)
