from functools import reduce

def Passar_a_Numero():
    llista = [3, 4, 1, 5]

    return reduce(lambda acc, digit: acc * 10 + digit, llista)


print(Passar_a_Numero())