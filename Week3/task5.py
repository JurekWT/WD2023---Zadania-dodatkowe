a = int(input())
b = ""
if a > 0:
    a = str(a)
    for i in range(len(a) - 1, 0 - 1, -1):
        b += a[i]
print(b)
