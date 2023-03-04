def listegrandchiffre(l, n):
    if n == 1:
        return l[0]
    return max(l[n-1], listegrandchiffre(l, n-1))

l = [0, 1, 2, 3, 4, 5, 26, 7, 8, 9]
n = len(l)

print(listegrandchiffre(l, n))  
