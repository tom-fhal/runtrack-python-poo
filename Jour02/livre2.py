class Livre():

    def __init__(self,titre,auteur, nbpages):
        self.titre = titre
        self.auteur = auteur 
        self.nbpages= nbpages 
        self.__disponible = True

    def set_livre(self):
        self.nouvtitre = input("Choisissez votre nouveau titre :")
        self.titre = self.nouvtitre
        self.nouvauteur = input("Choisissez votre nouveau auteur")
        self.auteur = self.nouvauteur 
        self.nouvnbpages = input("Choisissez vos nombres de pages")
        if type(self.nouvnbpages) == int():
            self.ngpages = self.nouvnbpages
        else:
            print("Erreur !")

    def get_livre(self):
        return self.titre, self.auteur,self.nbpages
    
    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
            print("Le livre est emprunté.")
        else:
            print("Le livre est pas disponible.")

    def rendre(self):
        if not self.__disponible:
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas été emprunté.")


livre1 = Livre("tomfhalproject","moi",23) 
livre1.set_livre()
print(livre1.get_livre())
livre1.verification()
livre1.emprunter()
livre1.rendre()