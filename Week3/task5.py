a = int(input())
a = str(a)
b = ""
for i in range(len(a)-1,0-1,-1):
    b += a[i]
print(b)
