from math import *




class Cercle():
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self):
        self.newrayon = 8
        self.rayon = self.newrayon
        print("Le rayon a ete changé voici le nouveau rayon :", self.rayon)

    def afficherInfos(self):
        print(self.rayon)
        print(Cercle.circonférence(self))
        print(Cercle.aire(self))
        print(Cercle.diametre(self))
    def circonférence(self):
        self.circonf = 2*pi*(self.rayon)
        print("La circonférence du cercle est :",self.circonf)

    def aire(self):
        self.airevaleur = pi*(self.rayon*self.rayon) 
        print("L'aire du cercle est de :",self.airevaleur)

    def diametre(self):
        self.diam = 2*(self.rayon)
        print("Le diamètre du cercle est de :",self.diam)
Cercle1 = Cercle(4)
Cercle2 = Cercle(7)
Cercle1.afficherInfos()
Cercle2.afficherInfos()

