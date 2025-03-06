def retorn_llista():
    llista = ["maria", "manta", "peu", "mà", "pyhton", "ordindaor"]

    lletra = input("Lletra: ")

    print(list(filter(lambda x: x[0].lower() in {lletra}, llista)))

retorn_llista()