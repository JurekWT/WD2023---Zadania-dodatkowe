# Zadanie A
A=[x for x in range(21) if x%2==0]
print(A)

# Zadanie B
B1 = 'jeden dwa trzy'
B1 = B1.split(' ')
B2 = [len(wyraz) for wyraz in B1]
print(B2)

# Zadanie C
C1 = [x for x in range(1,101) if x%3==0 and x%5==0]
print(C1)

# Zadanie D
D1 = 'pierwsze'
D2 = 'drugie'
D3 = set([litera for litera in D1+D2])
print(D3)

# Zadanie E
E1 = 'Przykładowe zdanie potrzebne do wykonania zadania'
E1 = E1.split(' ')
E2 = {wyraz:len(wyraz) for wyraz in E1}
print(E2)