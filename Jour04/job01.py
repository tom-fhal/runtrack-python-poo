class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("Age de la personne : ", self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, new_age):
        self.age = new_age


class Eleve(Personne):
    def __init__(self):
        super().__init__()

    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai", self.age, "ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        super().__init__()
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

eleve1 = Eleve()
print("Age par défaut de l'élève :", eleve1.age)
