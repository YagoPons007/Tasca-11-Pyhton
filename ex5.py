def enumerar():
    llista = ["casa", "cotxe", "taula", "cadira"]
    diccionari = {}
    for index, valor in enumerate(llista):
        diccionari[valor] = index
    return diccionari 
    
    
res = enumerar()
print(res)