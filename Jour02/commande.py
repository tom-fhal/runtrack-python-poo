class Commande:
    
    def __init__(self, numero):
        self.numero = numero
        self.plats = []
        self.statut = "en cours"
        
    def ajouter_plat(self, nom, prix):
        plat = {"nom": nom, "prix": prix, "statut": "commandé"}
        self.plats.append(plat)
    
    def calculer_total(self):
        return sum(plat["prix"] for plat in self.plats)
    
    def calculer_tva(self, taux):
        total = self.calculer_total()
        tva = total * taux / 100
        return tva
    
    def afficher(self):
        total = self.calculer_total()
        tva = self.calculer_tva(20)
        print(f"Commande numéro {self.numero}")
        for plat in self.plats:
            print(f"{plat['nom']} ({plat['statut']}) : {plat['prix']}")
        print(f"Total : {total}")
        print(f"TVA (20%) : {tva}")
        print(f"Total à payer : {total + tva}")
    
    def annuler(self):
        self.statut = "annulée"
        for plat in self.plats:
            plat["statut"] = "annulé"
    
    def modifier_statut_plat(self, nom_plat, nouveau_statut):
        for plat in self.plats:
            if plat["nom"] == nom_plat:
                plat["statut"] = nouveau_statut
                break

commande1 = Commande(1)
commande1.ajouter_plat("Steak frites", 15)
commande1.ajouter_plat("Salade César", 10)
commande1.ajouter_plat("Tarte aux pommes", 5)
commande1.afficher()
commande1.modifier_statut_plat("Salade César", "prêt")
commande1.annuler()