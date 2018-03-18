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

    def test_calcular_numero3(self):
        strProcess = '5,7'
        arrReturn = [0]
        arrReturn[0] = 2
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error en la prueba:")

    def test_calcular_numero4(self):
        strProcess = '5,7,0,9,0,1,3,5'
        arrReturn = [0]
        arrReturn[0] = 8
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error en la prueba:")

    # Iteracion 2
    def test_calcular_minimo1(self):
        strProcess = ''
        arrReturn = [1,1]
        arrReturn[0] = 0
        arrReturn[1] = 0
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error en la prueba:")

    def test_calcular_minimo2(self):
        strProcess = '1'
        arrReturn = [1, 1]
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error en la prueba:")

    def test_calcular_minimo3(self):
        strProcess = '2, 5'
        arrReturn = [2, 2]
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error en la prueba:")

    def test_calcular_minimo4(self):
        strProcess = '5,7,0,9,0,1,3,5'
        arrReturn = [8, 0]
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error en la prueba:")

    # Iteracion 3
    def test_calcular_maximo1(self):
        strProcess = ''
        arrReturn = [0,0,0]
        # arrReturn[0] = 1
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error en la prueba:")
