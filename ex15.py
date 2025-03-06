import random

def imprimir_tauler(tauler):
    for fila in tauler:
        print(" | ".join(fila))
        print("-" * 9)

def verificar_victoria(tauler, jugador):
    
    for i in range(3):
        if all(casella == jugador for casella in tauler[i]):  
            return True
        if all(tauler[j][i] == jugador for j in range(3)):  
            return True
    if tauler[0][0] == jugador and tauler[1][1] == jugador and tauler[2][2] == jugador:
        return True
    if tauler[0][2] == jugador and tauler[1][1] == jugador and tauler[2][0] == jugador:
        return True
    return False

def espai_disponible(tauler):
    for fila in tauler:
        if " " in fila:
            return True
    return False

def moure_jugador(tauler):
    while True:
        try:
            fila = int(input("Tria una fila (0, 1, 2): "))
            columna = int(input("Tria una columna (0, 1, 2): "))
            if tauler[fila][columna] == " ":
                return fila, columna
            else:
                print("Aquesta casella està ocupada, prova amb una altra.")
        except (ValueError, IndexError):
            print("Entrada no vàlida. Introdueix valors entre 0 i 2.")

def moure_maquina(tauler):
    moviments_disponibles = [(i, j) for i in range(3) for j in range(3) if tauler[i][j] == " "]
    return random.choice(moviments_disponibles)

def tres_en_ratlla():
    tauler = [[" " for _ in range(3)] for _ in range(3)]
    imprimir_tauler(tauler)

    mode = input("Vols jugar contra la màquina (1) o un altre jugador (2)? ")
    jugador_actual = "X"

    while True:
        print(f"Torn del jugador: {jugador_actual}")
        if mode == "1" and jugador_actual == "O":
            fila, columna = moure_maquina(tauler)
            print(f"La màquina ha triat: fila {fila}, columna {columna}")
        else:
            fila, columna = moure_jugador(tauler)
        tauler[fila][columna] = jugador_actual
        imprimir_tauler(tauler)

        if verificar_victoria(tauler, jugador_actual):
            print(f"Enhorabona! El jugador {jugador_actual} ha guanyat!")
            break
        if not espai_disponible(tauler):
            print("Empat! El tauler està ple.")
            break

        jugador_actual = "O" if jugador_actual == "X" else "X"

tres_en_ratlla()

