def retornar_valor():
    llista = [0, 1, 3, 3, 5, 5, 7, 8, 9, 10]
    contadodor = 0
    for num in enumerate(llista):
        if num[0] == num[1]:
            contadodor += 1
    return contadodor

print(retornar_valor())
    
