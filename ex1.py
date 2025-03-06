def longitud():
    frase = input("Frase: ")

    paraules = frase.split()

    longitud = list(map(len, paraules))

    print(longitud)

longitud()