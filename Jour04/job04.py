class Forme:
    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        return self.largeur * self.hauteur

# Créer un rectangle et calculer son aire
r = Rectangle(5, 3)
print("L'aire du rectangle est de :",r.aire())
