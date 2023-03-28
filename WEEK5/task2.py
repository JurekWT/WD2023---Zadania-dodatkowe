def czyPosortowana(lista):
    if lista == sorted(lista, reverse=1):
        return True
    else:
        return False


lista1 = [3, 4, 2, 3, 6, 7, 3]
lista2 = [8, 7, 6, 5, 4, 3, 2, 1]
print(czyPosortowana(lista1))
print(czyPosortowana(lista2))
