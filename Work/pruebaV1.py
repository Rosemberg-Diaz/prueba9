"""Rosemberg Daniel Diaz Mendez
19/10/2022

Codigo fuente Prueba9
Algoritmo para elevador de un edificio de 9 pisos sin bonus
"""


#Metodo para ingresar un piso a la lista de pisos cuando se encuentra en el mapa
def ingresarPiso(pisoActual, pisos, mapaPisos):
    pisoIngresar = ''
    #encontrar en cuales pisos se tiene que ingresar uno nuevo a la lista
    for piso in mapaPisos:
        if pisoActual == piso:
            pisoIngresar = mapaPisos[piso]
            #solo ingresa pisos a la lista cuando estos no estan ya en ella
            if pisoIngresar not in pisos:
                pisos.append(pisoIngresar)
                print("Piso ingresado: ",pisoIngresar)

#Metodo principal que gestiona el elevador
def elevador(pisoInicial, pisos, mapaPisos):
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
                    ingresarPiso(pisoActual, pisos, mapaPisos)

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
                    ingresarPiso(pisoActual, pisos, mapaPisos)

# Funcion main
if __name__ == '__main__':
    #piso donde se inicia el recorrido
    pisoInicial = 4
    #pisos a recorrer en su orden definido
    pisos = [5, 29, 13, 10]
    #mapa de pisos para ingresar nuevos
    mapaPisos =  {5:2, 29: 10, 13: 1, 10:1}
    #ejecucion del metodo principal que gestiona el elevador
    elevador(pisoInicial, pisos, mapaPisos)