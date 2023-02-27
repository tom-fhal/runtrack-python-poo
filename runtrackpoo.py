class Operation:

    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2= nombre2

    def addition(self):
        self.resultat= self.nombre1 + self.nombre2
        print(self.resultat)

op1=Operation(2,2)

op1.addition()
