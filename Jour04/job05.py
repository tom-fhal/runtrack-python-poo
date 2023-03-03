import math

class Forme:
    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        return self.largeur * self.hauteur


class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
    
    def aire(self):
        return math.pi * self.radius ** 2

# Créer une instance de chaque classe et calculer leur aire
r = Rectangle(5, 3)
c = Cercle(2)

print("L'aire du rectangle est de  :", r.aire())
print("L'aire du cercle est de:", c.aire())
