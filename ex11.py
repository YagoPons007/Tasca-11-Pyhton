def llegir_info():
    nom = input("Introdueix el nom del fitxer: ")
    try:    
        with open(nom, "r") as fitxer:
            print(fitxer.read())
    except FileNotFoundError:
        print("El fitxer no existeix")
    except IOError:
        return "Error: No s'ha pogut llegir el fitxer."
        
    
llegir_info()