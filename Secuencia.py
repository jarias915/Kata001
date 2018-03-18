#Test de commit de Wendell

class Secuencia:
    def calcular(self,sec):

        # Imprime la secuencia recibida
        print 'Cadena recibida:'
        print sec

        # Determina si la secuencia esta en blanco
        if sec == '':
            print 'La cadena recibida esta vacia.'
            arrReturn = []
            return arrReturn
