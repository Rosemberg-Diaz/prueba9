"""Rosemberg Daniel Diaz Mendez
19/10/2022

Codigo fuente Prueba9
Algoritmo para elevador de un edificio de 9 pisos bonus 2
"""

#metodo para solicitar elevador cuando el usuario lo desee añadiendolo a la lista
def solicitarElevador(pisos):
    #solicitud del piso
    pisoIngresar = int(input("Cual piso vas a solicitar?"))
    if pisoIngresar not in pisos:
        pisos.append(pisoIngresar)
        print("Piso solicitado: ", pisoIngresar)


#Metodo principal que gestiona el elevador
def elevador(pisoInicial, pisos):
    print("Elevador en el piso: ", pisoInicial)
    pisoActual = pisoInicial
    #recorrer lista de pisos hasta que quede vacia
    while len(pisos)>0:
        piso = pisos[0]
        if pisoActual < piso:
            #subir de piso hasta llegar al piso destino
            while pisoActual < piso:
                pisoActual += 1
                print("Elevador subiendo")
                print("Elevador en el piso: ", pisoActual)
                #mientras recorre los pisos comprobar si se pasa por algun otro que este en la lista
                if(pisoActual in pisos):
                    print("Elevador se detiene ")
                    pisos.remove(pisoActual)
                    opc = input(print("Solicitar elevador? Y/n"))
                    if (opc.upper() == 'Y'):
                        solicitarElevador(pisos)

        else:
            #bajar de piso hasta llegar al piso destino
            while pisoActual > piso:
                pisoActual -= 1
                print("Elevador descendiendo")
                print("Elevador en el piso: ", pisoActual)
                #mientras recorre los pisos comprobar si se pasa por algun otro que este en la lista
                if (pisoActual in pisos):
                    print("Elevador se detiene ")
                    pisos.remove(pisoActual)
                    opc=input(print("Solicitar elevador? Y/n"))
                    if(opc.upper()=='Y'):
                        solicitarElevador(pisos)

# Funcion main
if __name__ == '__main__':
    #piso donde se inicia el recorrido
    pisoInicial = 4
    #pisos a recorrer en su orden definido
    pisos = [5, 29, 13, 10]
    #ejecucion del metodo principal que gestiona el elevador
    elevador(pisoInicial, pisos)