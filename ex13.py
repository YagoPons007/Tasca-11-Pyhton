from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat

    @abstractmethod
    def xerrar(self):
        pass

    @abstractmethod
    def mourem(self):
        pass

    def quisoc(self):
        return f"Soc un {self.especie} i tinc {self.edat} anys."

class Cavall(Animal):
    def xerrar(self):
        return "Hiiiii"

    def mourem(self):
        return "Corre pel camp"

class Dofí(Animal):
    def xerrar(self):
        return "Eeeek eeeek"

    def mourem(self):
        return "Nada pel mar"

class Abella(Animal):
    def xerrar(self):
        return "Bzzz bzzz"

    def mourem(self):
        return "Vola de flor en flor"

    def picar(self):
        return "Pica i potser mor!"

class Humà(Animal):
    def __init__(self, especie, edat, nom):
        super().__init__(especie, edat)
        self.nom = nom

    def xerrar(self):
        return "Hola!"

    def mourem(self):
        return "Camina a dues cames"

class Fiet(Humà):
    def __init__(self, especie, edat, nom, pares):
        super().__init__(especie, edat, nom)
        self.pares = pares

    def nompares(self):
        return f"Els meus pares són: {', '.join(self.pares)}"

class Centaure(Cavall, Humà):
    def __init__(self, especie, edat, nom):
        Cavall.__init__(self, especie, edat)
        Humà.__init__(self, especie, edat, nom)

    def xerrar(self):
        return "Soc un centaure i parlo com un humà i un cavall."

    def mourem(self):
        return "Corro com un cavall i camino com un humà."

class Xou:
    def __init__(self, tipus):
        self.tipus = tipus

    def xerrar(self):
        return f"Soc un {self.tipus} fictici!"

    def mourem(self):
        return f"Em moc segons la meva imaginació."

    def quisoc(self):
        return f"Soc únic, un {self.tipus}."

# Crear elements de cada classe
elements = [
    Cavall("Cavall", 5),
    Dofí("Dofí", 8),
    Abella("Abella", 1),
    Humà("Humà", 30, "Maria"),
    Fiet("Humà", 12, "Pau", ["Joan", "Anna"]),
    Centaure("Centaure", 120, "Hèracles"),
    Xou("Criatura màgica")
]

# Executar un bucle per cridar els mètodes iguals
for element in elements:
    print(element.quisoc())
    print(element.xerrar())
    print(element.mourem())
    if isinstance(element, Abella):
        print(element.picar())
    if isinstance(element, Fiet):
        print(element.nompares())
