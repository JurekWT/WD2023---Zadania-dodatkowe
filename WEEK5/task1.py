def cq(n, a1=1, q=2):
    return a1 * q ** (n - 1)


print(cq(4))
print(cq(7, 5, 3))
