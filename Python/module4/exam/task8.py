n = int(input())
matrix = [[0]*n for _ in range(n)]

for j in range(n):
    for i in range(n-j):
        matrix[j+i][j] = i
        matrix[j][j+i] = i

def printMatrix(matriix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
        print()


printMatrix(matrix)


"""
if i == j -> 0

0 0 -> 0
1 0 0 1 -> 1
2 0 0 2 -> 2
3 0 0 3 -> 3
4 0 0 4 -> 4

1 1 -> 0
2 1 1 2 -> 1
3 1 1 3 -> 2
4 1 1 4 -> 3

"""
""""

0 1 2 3 4
1 0 1 2 3
2 1 0 1 2
3 2 1 0 1
4 3 2 1 0
"""