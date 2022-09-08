"""
    Para hacer los distintos escenarios decidí usar funciones que simbolizan cada escena que luego se ramifica en otras funciones.
    La idea original era poner un contador de vidas y que el juego estuviera todo dentro de un while vida > 0 con un monton de ifs, pero así es más cómodo de leer y jugar.
"""

import time

opciones = ["0", "1", "2", "3", "42"]

def verificar(dato):
    if dato == "42":
        print("-----------Larga vida a Zappick y al oraculo-----------")
        print("\n------------------------------------------")
        intro()
    while dato not in opciones:
        dato = input("Esa no es una opción válida, inténtalo de nuevo: ")
    return dato

def salir():
    print("\n¡Gracias por jugar!")
    print("\n¿Quieres volver a intentarlo? sí/no")
    opcion = input(">")
    if opcion.lower() == "si" or opcion.lower() == "s":
        print("\n¡Bien dicho! ¡Volvamos a intentarlo!")
        print("\n------------------------------------------")
        escena_inicial()
    elif opcion.lower() == "no" or opcion.lower() == "n":
        print("\nQue lastima, ¡Nos vemos en otra ocasion!")
    else:
        print("Esa no es una opcion valida, vuelve a intentarlo.")
        print("\n------------------------------------------")
        salir()

def intro():
    print("\nBienvenido/a a 'La cueva', un pequeño juego basado en texto donde descubriras el misterio de la extraña cueva donde te encuentras.")
    time.sleep(2) #time.sleep() me deja dar un espacio de pocos segundos para dejar al usuario leer de manera más cómoda
    print("\nDurante todo el juego se te presentaran desafios que tendrás que resolver eligiendo una de las opciones que te aparecen en pantalla,")
    print("recuerda que unicamente debes utilizar los numeros indicados para resolver los problemas, si no lo haces no podrás progresar.")
    time.sleep(4)
    print("\nTendrás la opción de salir disponible en todo momento por si te aburres del juego.")
    time.sleep(2)
    print("¿Estás listo/a para jugar? sí/no")
    opcion = input(">")
    if opcion.lower() == "si" or opcion.lower() == "s":
        print("¡Perfecto! Comencemos.")
        escena_inicial()
    elif opcion.lower() == "no" or opcion.lower() == "n":
        print("¡Que lástima! Nos vemos en otra ocasion.")
    else:
        print("Esa no es una opcion valida, vuelve a intentarlo.")
        print("\n------------------------------------------")
        intro()

def escena_inicial():
    print("\n------------------------------------------")
    print("\nUnas gotas caen en tu frente y te hacen despertar. Al mirar a tu alrededor te das cuenta que te encuentras en una cueva oscura donde apenas puedes ver por delante de tu nariz.")
    print("Te levantas y notas que lo unico que tienes es la ropa que llevabas puesta mientras dormias, ¿Será esto un sueño?")
    print("Enfrente tuyo tienes la continuacion de la cueva, aunque tal vez no sea la mejor de las ideas... ")
    print("\n¿Que haras?")
    time.sleep(1)
    print("1 - Seguir adelante")
    print("2 - Inspeccionas la zona")
    print("3 - Volver atras")
    print("0 - Salir del juego")
    opcion = input(">")
    opcion = verificar(opcion)
    if opcion == "1":
        print("\nDecides seguir adelante y adentrarte más en la cueva y sus secretos...")
        escena_adentrarse()
    elif opcion == "2":
        print("\nDecides observar con más atencion tus alrededores...")
        escena_alrededores()
    elif opcion == "3":
        print("\nDecides darte la vuelta...")
        escena_atras()
    elif opcion == "0":
        salir()

def escena_adentrarse():
    print("Caminando descubres una nueva sala con una puerta de madera al final de la misma, la puerta tiene tres botones:")
    print("El primero tiene una luna llena.")
    print("El segundo tiene una luna creciente.")
    print("Y el tercero tiene una luna nueva.")
    print("\n¿Cual presionas?")
    time.sleep(1)
    print("1 - El primero")
    print("2 - El segundo")
    print("3 - El tercero")
    print("0 - Salir del juego")
    opcion = input(">")
    opcion = verificar(opcion)
    if opcion == "1":
        print("\nPresionas el primer boton...")
        boton_1()
    elif opcion == "2":
        print("\nPresionas el segundo boton...")
        boton_2()
    elif opcion == "3":
        print("\nPresionas el tercer boton...")
        boton_3()
    elif opcion == "0":
        salir()

def boton_1():
    print("Y la puerta se abre, dejandote ver un brillo intenso que te ciega momentaneamente.")
    print("Una vez el brillo se apaga abres los ojos y ves que estas en una playa en la noche, sin ninguna señal de la cueva.")
    time.sleep(1)
    print("\n-----------EL FIN-----------")
    time.sleep(1)
    salir()

def boton_2():
    print("Y la puerta se abre, dejandote ver tu cuarto a oscuras.")
    print("Atraviesas la puerta y esta se cierra detras de ti, dejandote finalmente en tu habitación.")
    time.sleep(1)
    print("\n-----------EL FIN-----------")
    time.sleep(1)
    salir()

def boton_3():
    print("Y la puerta se abre, dejandote ver una gran negrura enfrente tuyo la cual atraviesas.")
    print("Tras caminar unos minutos encuentras otra puerta que te lleva a tu habitacion, pero ves tu cuerpo durmiendo en tu cama y tu no puedes hacer nada...")
    time.sleep(1)
    print("\n-----------PERDISTE-----------")
    time.sleep(1)
    salir()

def escena_alrededores():
    print("¡Y un monstruo te sorprende! ¡Sera mejor que huyas!")
    print("Corres hacia adelante y te encuentras una espada tirada en el suelo, aunque tambien hay una puerta cerrada.")
    print("\n¿Que haras?")
    time.sleep(1)
    print("1 - Agarrar la espada")
    print("2 - Correr hacia la puerta")
    print("3 - Hacerle frente al monstruo")
    print("0 - Salir del juego")
    opcion = input(">")
    opcion = verificar(opcion)
    if opcion == "1":
        print("\nTe apresuras para agarrar la espada...")
        escena_espada()
    elif opcion == "2":
        print("\nVas corriendo hacia la puerta...")
        escena_puerta()
    elif opcion == "3":
        print("\nTe das la vuelta y miras firmemente al monstruo...")
        escena_enfrentar()
    elif opcion == "0":
        salir()

def escena_espada():
    print("Y cuando vas a golpear con ella al monstruo esta se parte, dejandote indefenso.")
    print("El monstruo se ríe de tu intento mientras te come.")
    time.sleep(1)
    print("\n-----------PERDISTE-----------")
    time.sleep(1)
    salir()

def escena_puerta():
    print("¡Pero cuando tratas de abrirla te das cuenta que esta cerrada!")
    print("Miras hacia atras mientras el monstruo se acerca lentamente para comerte...")
    time.sleep(1)
    print("\n-----------PERDISTE-----------")
    time.sleep(1)
    salir()

def escena_enfrentar():
    print("Para tu sorpresa, este se detiene ante tu valentia y a modo de reconocimiento te explica la forma de salir de este lugar.")
    print("Mientras te explica todo sientes un cosquilleo por todo tu cuerpo y terminas despertando en tu cama, se ve que todo fue un sueño muy raro...")
    time.sleep(1)
    print("\n-----------EL FIN-----------")
    time.sleep(1)
    salir()

def escena_atras():
    print("Y lo que ven tus ojos te sorprende. ¡Una escalera hacia el techo de la cueva!")
    print("Comienzas a escalar la escalera y al cabo de unos minutos sales de la misma terminando en un hermoso campo con flores.")
    time.sleep(1)
    print("\n-----------EL FIN-----------")
    time.sleep(1)
    salir()

intro()