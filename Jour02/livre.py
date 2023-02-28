class Livre():

    def __init__(self,titre,auteur, nbpages):
        self.titre = titre
        self.auteur = auteur 
        self.nbpages= nbpages 

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
        

livre1 = Livre("tomfhalproject","moi",23,"") 
livre1.set_livre()
print(livre1.get_livre())
    