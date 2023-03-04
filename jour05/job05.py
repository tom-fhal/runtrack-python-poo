def fibosuite(x):
    if x <= 1:
        return x
    else:
        return (fibosuite(x-1) + fibosuite(x-2))
    
x = int(input("Quel nombre voulez-vous calculer ?"))
print(fibosuite(x))