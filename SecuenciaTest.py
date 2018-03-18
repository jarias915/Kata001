from unittest import TestCase

from Secuencia import Secuencia

class SecuenciaTest(TestCase):

    # Iteracion 1
    def test_calcular_numero1(self):
        strProcess = ''
        arrReturn = [0,0,0,0]
        #arrReturn[0] = 1
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error en la prueba:")

    def test_calcular_numero2(self):
        strProcess = '1'
        arrReturn = [1, 1, 1, 1]
        #arrReturn[0] = 1
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error en la prueba:")

    def test_calcular_numero3(self):
        strProcess = '5,7'
        arrReturn = [2, 5, 7, 6]
        #arrReturn[0] = 2
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error en la prueba:")

    def test_calcular_numero4(self):
        strProcess = '5,7,0,9,0,1,3,5'
        arrReturn = [8, 0, 9, 3]
        #arrReturn[0] = 8
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error en la prueba:")

    # Iteracion 2
    def test_calcular_minimo1(self):
        strProcess = ''
        arrReturn = [0,0,0,0]
        #arrReturn[0] = 0
        #arrReturn[1] = 0
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error en la prueba:")

    def test_calcular_minimo2(self):
        strProcess = '1'
        arrReturn = [1, 1, 1, 1]
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error en la prueba:")

    def test_calcular_minimo3(self):
        strProcess = '2, 5'
        arrReturn = [2, 2, 5, 3]
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error en la prueba:")

    def test_calcular_minimo4(self):
        strProcess = '5,7,0,9,0,1,3,5'
        arrReturn = [8, 0,9,3]
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error en la prueba:")

    # Iteracion 3
    def test_calcular_maximo1(self):
        strProcess = ''
        arrReturn = [0,0,0,0]
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error en la prueba:")

    def test_calcular_maximo2(self):
        strProcess = '3'
        arrReturn = [1,3,3,3]
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error un numero:")

    def test_calcular_maximo3(self):
        strProcess = '3,4'
        arrReturn = [2,3,4,3]
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error dos numeros ")

    def test_calcular_maximo4(self):
        strProcess = '6,3,2,5,3'
        arrReturn = [5,2,6,3]
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error N numeros:")


    # Iteracion 4
    def test_calcular_promedio1(self):
        strProcess = ''
        arrReturn = [0,0,0,0]
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error string vacio:")

    def test_calcular_promedio2(self):
        strProcess = '4'
        arrReturn = [1,4,4,4]
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error un numero:")

    def test_calcular_promedio3(self):
        strProcess = '4,2'
        arrReturn = [2,2,4,3]
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error prueba  promedio 2 numeros :")

    def test_calcular_promedio4(self):
        strProcess = '5,3,7,8,2'
        arrReturn = [5,2,8,5]
        self.assertEqual(Secuencia().calcular(strProcess), arrReturn, "Error prueba promedio  n numeros:")