class Personne:

    def __init__ (self,prenom,nom):
        self.nom = nom
        self.prenom= prenom

    def Sepresenter(self):
        print("Je suis",self.prenom,self.nom)

presentation1=Personne("Tom","Fhal")
presentation1.Sepresenter()