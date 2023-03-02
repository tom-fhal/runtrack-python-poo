class CompteBancaire:
    def __init__(self, nb_compte, nom, prenom, solde, decouvert):
        self.__nb_compte = nb_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
    
    def afficher(self):
        print("Numéro de compte : {}\nNom : {}\nPrénom : {}\nSolde : {}".format(self.__nb_compte, self.__nom, self.__prenom, self.__solde))

    def afficher_solde(self):
        print("Solde : {}".format(self.__solde))
    
    def versement(self, montant):
        if isinstance(montant, int):
            self.__solde += montant
        else:
            print("Le montant doit être un nombre entier")

    def retrait(self, montant):
        if self.__decouvert:
            if isinstance(montant, int):
                self.__solde -= montant
                return True
            else:
                print("Le montant doit être un nombre entier") 
        else:
            if isinstance(montant, int):
                if self.__solde > montant:
                    self.__solde -= montant
                    return True
                else:
                    print("vous n'avez pas assez de solde disponible")
            else:
                print("Le montant doit être un nombre entier")
            
    def set_decouvert(self, boolean):
        self.__decouvert = boolean

    def agios(self):
        if self.__solde < 0:
            self.__solde -= self.__solde * 0.07

    def virement(self, compte_crediter, montant):
        if self.retrait(montant):
            compte_crediter.versement(montant)
            print("Virement effectué")
        else:
            print("Le virement n'a pas été accepté !")

compte1 = CompteBancaire(3567, 'Mark', 'Zuckerberg', 28889, False)
compte1.afficher()
compte1.afficher_solde()
compte1.versement('banane')
compte1.versement(150)
compte1.afficher_solde()
compte1.retrait(500)
compte1.afficher_solde()
compte1.retrait(4000)
compte1.set_decouvert(True)
compte1.retrait(4000)
compte1.afficher_solde()
compte2 = CompteBancaire(12344, 'Thomas', 'Jordan', 123, True)
compte1.versement(4000)
compte1.set_decouvert(False)
compte1.virement(compte2, 15000)
compte1.virement(compte2, 120)
compte2.afficher_solde()
