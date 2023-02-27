class Point:

    def __init__(self,x ,y):
        self.largeur = x
        self.hauteur = y

    def afficherLesPoints(self):
        print(self.largeur,self.hauteur)

    def afficherX(self):
        print(self.largeur)
    
    def afficherY(self):
        print(self.hauteur)

    def changerX(self, x2):
        self.largeur = x2
        print(x2)
    
    def changerY(self, y2):
        self.hauteur = y2
        print(y2)

cord1 =Point(8,3)
cord1.afficherLesPoints()
cord1.afficherX()
cord1.afficherY()
cord1.changerX(5)
cord1.changerY(7)