class Vehicule:
    def __init__(self, marque, annee, prix,modele):
        self.marque = marque
        self.annee = annee
        self.prix = prix
        self.modele = modele

    def informationsVehicule(self):
        print("Marque :", self.marque)
        print("Année :", self.annee)
        print("Prix :", self.prix)
        print("Modele :", self.modele)

    def demarrer(self):
        print("Attention, je roule !")

class Voiture(Vehicule):
    def __init__(self, marque, annee,modele, prix,portes = 4):
        super().__init__(marque, annee, prix,modele)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes :", self.portes)

    def demarrer(self):
        print("Je démarre ma voiture.")

class Moto(Vehicule):
    def __init__(self, marque, annee, prix,modele,roue = 2):
        super().__init__(marque, annee, prix,modele)
        self.roue = roue

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de roues :", self.roue)

    def demarrer(self):
        print("Je démarre ma moto.")

# Instanciation d'un objet Voiture
voiture1 = Voiture("Mercede", 2010, 50000,2,4)
voiture1.informationsVehicule()
voiture1.demarrer()

# Instanciation d'un objet Moto
moto1 = Moto("Ducatti", 2009, 21000,2)
moto1.informationsVehicule()
moto1.demarrer()
