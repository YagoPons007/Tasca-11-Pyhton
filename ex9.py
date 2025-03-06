llista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
potencia = int(input("Intrpodueix una potència: "))
llista_res = [nombre ** potencia for nombre in llista]
print(llista_res)