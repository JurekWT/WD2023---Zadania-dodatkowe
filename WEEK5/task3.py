def suma_kwadratow(*args):
    suma = 0
    for i in range(len(args)):
        suma += args[i] ** 2
    return suma


a = 3
b = 6
c = 2
print(suma_kwadratow(a, b, c))
print(suma_kwadratow(2, 2, 2))