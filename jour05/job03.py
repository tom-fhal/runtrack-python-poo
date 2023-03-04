def caractère(chaine):
    if not chaine:
        return 0
    else : 
        return 1+ caractère(chaine[1:])
    
chaine = "123456789101112"
print(caractère(chaine))