a = [(i, j) for i in range(3) for j in range(4)]
print(a)

M, N = 3, 4
matrix = [[a for a in range(M)] for b in range(N)]
print(matrix)

A = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
A = [[x ** 2 for x in row] for row in A]
print(A)

g = [u ** 2 for u in [x + 1 for x in range(5)]]
print(g)
