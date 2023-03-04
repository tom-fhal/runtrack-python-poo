def factorielle(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x *factorielle(x-1)

x =int(input("Renseignez le nombre entier au programme :"))
resultat = factorielle(x)
print(resultat)