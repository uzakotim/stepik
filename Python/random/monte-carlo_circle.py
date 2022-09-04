import random

n = 10**6       # количество испытаний
s0 = 4
k = 0
for _ in range(n):
    x = random.uniform(-1.0,1.0)
    y = random.uniform(-1.0,1.0)
    if (x**2 + y**2)<=1:
        k+=1

print(k*s0/n)
