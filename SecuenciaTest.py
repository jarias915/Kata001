from unittest import TestCase

from Secuencia import Secuencia

class SecuenciaTest(TestCase):

    # Iteracion 1
    def test_calcular_numero1(self):
        strProcess = ''
        arrReturn = []
        #arrReturn[0] = 1
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error en la prueba:")

    def test_calcular_numero2(self):
        strProcess = '1'
        arrReturn = [0]
        arrReturn[0] = 1
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error en la prueba:")
