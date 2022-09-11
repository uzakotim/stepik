from tkinter import N


def matrix(n=1,m=-1,value=0):
    mtx = []
    if (m<0):
        m = n
    for _ in range(n):
        temp = []
        for _ in range(m):
            temp.append(value)
        mtx.append(temp)
    return mtx

print(matrix())                   # матрица 1 × 1 из 0
print(matrix(3))                  # матрица 3 × 3 из 0
print(matrix(2, 5))               # матрица 2 × 5 из 0
print(matrix(3, 4, 9))            # матрица 3 × 4 из 9