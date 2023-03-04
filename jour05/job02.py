def puissance(x,n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        y = puissance(x, n/2)
        return y * y
    else:
        return x * puissance(x, n-1)

x =int(input("Renseignez le nombre x entier au programme :"))
n =int(input("Renseignez le nombre y entier au programme :"))
resultat = puissance(x, n)
print(resultat)