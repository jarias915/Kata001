#Test de commit de Wendell

class Secuencia:
    def calcular(self,sec):

        # Imprime la secuencia recibida
        print ('Cadena recibida:')
        print (sec)

        # Determina si la secuencia esta en blanco
        if sec == '':
            print ('La cadena recibida esta vacia.')
            arrReturn = [1,1, 1,1]
            arrReturn[0] = 0
            arrReturn[1] = 0
            arrReturn[2] = 0
            arrReturn[3] = 0
            return arrReturn

        # Python se comporta de manera especial cuando se hace Split sobre una cadena en blanco, por lo que la siguiente
        # linea de ejecucion genera un arreglo que si tiene un elemento, por lo que se debe tener en cuenta en la prueba
        # arrProcess = sec.split(",")

        # Al hacer el split de la secuencia se genera un array de Strings, toca hacer el cast a int
        arrProcess = [int(x) for x in sec.split(",")]

        # Determina el numero de elementos en la cadena
        num_elementos = len(arrProcess)
        print ('Numero de elementos en la cadena:')
        print (num_elementos)

        # Asigna el arreglo que se va a retornar
        arrReturn = [0,0,0,0]
        arrReturn[0] = num_elementos

        # Imprime el arreglo que se va a retornar
        print ('Arrego con numero de elementos:')
        print (arrReturn[0])

        #Asigna el minimo numero del arreglo
        arrReturn[1] = min(arrProcess)

        #Asigna el maximo numero del arreglo
        arrReturn[2] = max(arrProcess)

        #Asigna el promedio
        arrReturn[3] = sum(arrProcess) / num_elementos

        # Retorna el arreglo
        return arrReturn
