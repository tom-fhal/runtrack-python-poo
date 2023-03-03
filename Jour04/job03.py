class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    
    def volume(self):
        return self.surface() * self.__hauteur
    
    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

r1 = Rectangle(2, 9)
print("Périmètre :", r1.perimetre())
print("Surface :", r1.surface())
r1.set_longueur(8)
r1.set_largeur(12)
print("Longueur :", r1.get_longueur())
print("Largeur :", r1.get_largeur())
p1 = Parallelepipede(5, 3, 2)
print("Volume :", p1.volume())
p1.set_hauteur(6)
print("Hauteur :", p1.get_hauteur())
