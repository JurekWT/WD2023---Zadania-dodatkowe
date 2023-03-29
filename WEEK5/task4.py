def srednia_wieku(**kwargs):
    suma = 0
    for key, value in kwargs.items():
        suma += kwargs[key]
    srednia = suma / len(kwargs)
    return srednia


print(srednia_wieku(Roman=34, Stefan=23, Zenon=45, Wiesiek=15))
print(srednia_wieku(Jace=10, Placek=10))
