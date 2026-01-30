"""Problem:
In a bubble shooting game, there are N*N bubbles in Red, Green, and Blue. The program must accept a character matrix of size N*N representing the colors of the bubbles and Q queries as input. Each query contains three values: D, P, and C.
- D represents the direction in which the player can shoot (L - Left, R - Right, T - Top, B - Bottom).
- P represents the position of a row or column in which the player can shoot.
- C represents the color of the bullet given to the player.

Rules:
- The player can shoot a bubble using a bullet with the same color in the specified direction D and the specified position P.
- If two or more bubbles have the same color, then the first occurring bubble in the specified direction will explode.
- If there is no bubble to shoot with the given bullet, then the player will ignore the bullet.
- The program must print the modified matrix and the number of bullets ignored.
- Empty spaces in the matrix must be replaced with asterisks (*).

Boundary Conditions:
2 <= N <= 50
1 <= P <= N
1 <= Q <= 1000

Input Format:
- The first line contains N.
- The next N lines, each contains N characters separated by a space representing the colors of the bubbles.
- The N+2nd line contains Q.
- The next Q lines, each contains D, P, and C separated by a space.

Output Format:
- The first N lines, each contains N characters separated by a space.
- The N+1st line contains an integer representing the number of bullets the player ignored.

Example:
Input:
4
R G B R
G B R G
B R G B
R G B R
3
T 2 G
R 3 R
L 1 B

Output:
R * B R
G B * G
B R G B
R G B R
1
"""
n = int(input())
matrix = [input().split() for _ in range(n)]
q = int(input())
ignored = 0

for _ in range(q):
    d, p, c = input().split()
    p = int(p) - 1
    exploded = False

    if d == 'T':
        for i in range(n):
            if matrix[i][p] == c:
                matrix[i][p] = '*'
                exploded = True
                break
    elif d == 'B':
        for i in range(n - 1, -1, -1):
            if matrix[i][p] == c:
                matrix[i][p] = '*'
                exploded = True
                break
    elif d == 'L':
        for i in range(n - 1, -1, -1):
            if matrix[p][i] == c:
                matrix[p][i] = '*'
                exploded = True
                break
    elif d == 'R':
        for i in range(n):
            if matrix[p][i] == c:
                matrix[p][i] = '*'
                exploded = True
                break

    if not exploded:
        ignored += 1

for row in matrix:
    print(' '.join(row))
print(ignored)
