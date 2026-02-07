# The program must accept a character matrix of size R x C and an integer K as input.
# The matrix contains only lowercase alphabets.
# The values of R and C are always divisible by K.
# For each K x K submatrix in the given matrix, the program must sort the alphabets
# in that submatrix in alphabetical order.
# Then the program must print the revised matrix as output.
#
# Boundary Conditions:
# 2 ≤ R, C, K ≤ 50

R, C = map(int, input().split())

matrix = []
for _ in range(R):
    row = input().strip()
    matrix.append(list(row))

K = int(input())

for i in range(0, R, K):
    for j in range(0, C, K):
        block = []
        for x in range(i, i + K):
            for y in range(j, j + K):
                block.append(matrix[x][y])

        block.sort()

        idx = 0
        for x in range(i, i + K):
            for y in range(j, j + K):
                matrix[x][y] = block[idx]
                idx += 1

for row in matrix:
    print("".join(row))
