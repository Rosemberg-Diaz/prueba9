"""Rosemberg Daniel Diaz Mendez
19/10/2022

Codigo fuente Prueba9
Algoritmo para elevador de un edificio de 9 pisos bonus 3
"""
# metodo para solicitar elevador cuando el usuario lo desee añadiendolo a la lista
def solicitarElevador(pisos):
    # solicitud del piso
    pisoIngresar = int(input("Cual piso vas a solicitar?"))
    if pisoIngresar not in pisos:
        pisos.append(pisoIngresar)
        print("Piso solicitado: ", pisoIngresar)

#metodo para conocer cual piso es el mas cercano al actual
def conocerPisoDestino(pisos, pisoActual):
    #lista para guardar la diferencia de pisos en todos los casos
    numeroPisosRecorrer = []
    #calcular todas las diferencias de pisos frente al actual
    for piso in pisos:
        diferencia = piso - pisoActual
        numeroPisosRecorrer.append(abs(diferencia))
    #conocer cual piso es el destino que tenga menos recorrido
    for piso in range(len(numeroPisosRecorrer)):
        if numeroPisosRecorrer[piso] == min(numeroPisosRecorrer):
            return pisos[piso]

#metodo para recorrer los pisos
def elevador(pisos,nombre, pisoActual, piso):
    if pisoActual < piso:
        # subir de piso hasta llegar al piso destino
        while pisoActual < piso:
            pisoActual += 1
            print("Elevador ", nombre," subiendo")
            print("Elevador ", nombre," en el piso: ", pisoActual)
        print("Elevador ", nombre," se detiene ")
        pisos.remove(piso)
        #solicitar elevador
        opc = input(print("Solicitar elevador? Y/n"))
        if (opc.upper() == 'Y'):
            solicitarElevador(pisos)

    else:
        # bajar de piso hasta llegar al piso destino
        while pisoActual > piso:
            pisoActual -= 1
            print("Elevador ", nombre," descendiendo")
            print("Elevador ", nombre," en el piso: ", pisoActual)
        print("Elevador ", nombre," se detiene ")
        pisos.remove(piso)
        # solicitar elevador
        opc=input(print("Solicitar elevador? Y/n"))
        if(opc.upper()=='Y'):
            solicitarElevador(pisos)

#Metodo principal que gestiona el elevador
def gestionSolicitudes(pisos, pisoInicialUno,pisoInicialDos, nombreUno, nombreDos):
    print("Elevador ", nombreUno, " en el piso: ", pisoInicialUno)
    print("Elevador ", nombreDos, " en el piso: ", pisoInicialDos)
    pisoActualUno = pisoInicialUno
    pisoActualDos = pisoInicialDos
    #recorrer lista de pisos hasta que quede vacia
    while len(pisos)>0:
        #definir cada que cambia el piso a donde debe ir cada elevador
        pisoUno = conocerPisoDestino(pisos,pisoActualUno)
        elevador(pisos,nombreUno,pisoActualUno,pisoUno)
        pisoActualUno = pisoUno
        pisoDos = conocerPisoDestino(pisos, pisoActualDos)
        elevador(pisos,nombreDos, pisoActualDos,pisoDos)
        pisoActualDos = pisoDos



# Funcion main
if __name__ == '__main__':
    # piso donde se inicia el recorrido
    pisoInicialUno = 4
    pisoInicialDos = 20
    pisos = [5, 29, 13, 10]
    gestionSolicitudes(pisos, pisoInicialUno,pisoInicialDos, "A", "B")
    # pisos a recorrer en su orden definido
    #ejecucion del metodo principal que gestiona el elevador