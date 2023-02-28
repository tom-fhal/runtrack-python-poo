class Rectangle():
    def __init__ (self, longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    def set_rectangle(self):
        self.longueur = 10
        self.largeur = 5
        print("La longueur est:",self.longueur)
        print("La largeur est :",self.largeur)
     
 
    # Defining Accessor Method
    def get_rectangle(self):
        return self.longueur, self.largeur
    
rec1=Rectangle(19,5)
rec1.set_rectangle()
rec1.get_rectangle()
    
