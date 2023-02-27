class produit():
    def __init__(self, nom,prixHT,TVA):
        self.nom = nom
        self.prixHT= prixHT
        self.TVA = TVA


    def CalculerprixTTC(self):
        self.prixTTC = int(self.prixHT) + int(self.TVA)
        print("Le prix TTC est de :",self.prixTTC)

    def afficher(self):
        print("Nom du produit : ",self.nom)
        print("Prix HT : ",self.prixHT)
        print("TVA :",self.TVA)

    def modifier(self):
        self.newnom = input("entrez le nouveau nom")
        self.nom = self.newnom
        self.newprix = input("entre le nouveau prix")
        self.prixHT = self.newprix
        produit.CalculerprixTTC(self)
        print(produit.afficher(self))
produit1= produit("MMS",3,0.4)
produit1.modifier()
