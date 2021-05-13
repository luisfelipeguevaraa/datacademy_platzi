## ################################
## RETO 2 - PIEDRA, PAPEL O TIJERA
## ################################
def run():
    jugadas = ["piedra", "papel", "tijera"]
    #Ingreso de datos
    print("-- PIEDRA PAPEL O TIJERA")
    print("-- ingrese jugada:\n--   piedra \n--   papel \n--   tijera")
    jugada1 = input("Jugador 1, Ingreso jugada: ")
    validarJugada(jugada1, jugadas)
    jugada2 = input("Jugador 2, Ingreso jugada: ")
    validarJugada(jugada2, jugadas)

    resultado = "empate"
    #calcular ganador
    if (jugada1 == "papel" and jugada2 == "piedra") or (jugada1 == "piedra" and jugada2 == "tijera") or (jugada1 == "tijera" and jugada2 == "papel") :
        resultado = "gana jugador 1"
    if (jugada2 == "papel" and jugada1 == "piedra") or (jugada2 == "piedra" and jugada1 == "tijera") or (jugada2 == "tijera" and jugada1 == "papel") :
        resultado = "gana jugador 2"
    print(resultado)

def validarJugada(jugada, jugadas):
    listValid = list(filter(lambda j: j == jugada, jugadas))
    if not listValid:
         raise Exception("no es una jugada valida")

if __name__ == '__main__':
    run()