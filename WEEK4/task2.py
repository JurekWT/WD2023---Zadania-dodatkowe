import random

random.seed(106783)
rlist = [random.randrange(1, 101) for x in range(200)]
print(rlist)

# Zadanie 1
print('Zadanie 1')
suma = 0
for x in rlist:
    suma += x
print(suma)

# Zadanie 2
print('Zadanie 2')
min1 = rlist[0]
for i in rlist:
    if min1 > rlist[i]:
        min1 = rlist[i]
print(min1)
min2 = min(rlist)
print(min2)

# Zadanie 3
print("Zadanie 3")
max1 = rlist[0]
for i in rlist:
    if max1 < rlist[i]:
        max1 = rlist[i]
print(max1)
max2 = max(rlist)
print(max2)

# Zadanie 4
print('Zadanie 4')
M1 = sorted(rlist)
if len(M1) % 2 == 0:
    M2 = (M1[int(len(M1) / 2)] + M1[int(len(M1) / 2 - 1)]) / 2
else:
    M2 = M1[int(len(M1) / 2)]
print(M2)

# Zadanie 5
print('Zadanie 5')
S5 = sorted(rlist)
print(S5[:20])
for x in range(20):
    print(S5[x])

# Zadanie 6
print('Zadanie 6')
I1 = 1
for i in rlist:
    I1 *= rlist[i]
print(I1)

# Zadanie 7
print('Zadanie 7')
liczbyDwucyfrowe = 0
for i in rlist:
    if len(str(rlist[i])) == 2:
        liczbyDwucyfrowe += 1
print(liczbyDwucyfrowe)

# Zadanie 8
print('Zadanie 8')
iloscPowtorzen = {cyfra: rlist.count(cyfra) for cyfra in rlist}
maxPowtorzen = max(iloscPowtorzen, key=iloscPowtorzen.get)
print(maxPowtorzen, iloscPowtorzen[maxPowtorzen])

# Zadanie 9
print('Zadanie 9')
P9 = {x: rlist.count(x) for x in rlist}
for x in P9:
    if P9[x] == 1:
        print(x)

# Zadanie 10
print('Zadanie 10')
P10 = {liczba: rlist.count(liczba) for liczba in rlist}
L10 = [x for x in P10 if P10[x] == 3]
print(L10)

# Zadanie 11
print('Zadanie 11')
Z11 = 0
for i in rlist:
    if rlist[i] > 27:
        Z11 += 1
print(Z11)
