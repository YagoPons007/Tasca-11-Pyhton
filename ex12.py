with open("/home/cicles/AO/Prova/Ex12.txt", "a") as fitxer:
    for i in range(6):
        noms = input("Introdueix el nom dels professors: ")

        fitxer.write(noms + "\n")


with open("/home/cicles/AO/Prova/Ex12.txt", "r") as fitxer:
    llista = [linia.strip() for linia in fitxer]

print(llista)