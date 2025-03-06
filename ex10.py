def divisio_0():
    dividend = int(input("Introdueix el dividend: "))
    divisor = int(input("Introdueix el divisor: "))
    try:
        resultat = dividend / divisor
        print(resultat)
    except ZeroDivisionError:
        print("No es pot dividir per zero")
divisio_0()