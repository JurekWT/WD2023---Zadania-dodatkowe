def sumaKwadratow(*args):
    suma = 0
    for i in range(len(args)):
        suma += args[i] ** 2
    return suma


a = 3
b = 6
c = 2
print(sumaKwadratow(a, b, c))
print(sumaKwadratow(2, 2, 2))