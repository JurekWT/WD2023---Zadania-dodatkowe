n = int(input())
m = int(input())
for i in range(1, m):
    if n * i < m and n * i > 0:
        print(n * i)
