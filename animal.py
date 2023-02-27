class Animale:
    def  __init__(self, age, prenom):
        self.age = age
        self.prenom = prenom

    def Vieillir(self):
        print("L'age de l'animal :",self.age)
        print("L'age de l'animal :",self.age+1)
        
    def nommer(self):
        print("L'animal s'appelle",self.prenom)

animale1 = Animale(8,"Braudy")
animale1.Vieillir()
animale1.nommer()
