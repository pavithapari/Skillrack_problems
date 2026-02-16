"""Problem:
The program must accept the coordinates (x, y) of N points on a graph as the input. 
The program must print the number of squares that can be formed parallel to the axes as the output.
Note: Ignore the duplicate coordinates when finding the squares.
Boundary Conditions:
4 <= N <= 500
-10 <= x, y <= 10
Input Format:
The first line contains N.
The next N lines, each contains the coordinates (x, y) of a point on a graph.
Output Format:
The first line contains the number of squares that can be formed parallel to the axes.
Example Input/Output 1:
Input:
5
0 0
0 2
2 2
2 0
1 1

Output:
1

Explanation:
The only square is formed using the points (0, 0), (0, 2), (2, 2) and (2, 0).

Example Input/Output 2:
Input:
13
-2 2
-1 2
-2 1
-1 1
2 2
2 1
1 2
1 1
2 0
1 0
0 0
0 1
-1 -1

Output:
2"""
n = int(input())
points = set(tuple(map(int, input().split())) for _ in range(n))

squares = set()

for p1 in points:
    for p2 in points:
        if p1 == p2:
            continue
        x1, y1 = p1
        x2, y2 = p2

        # Horizontal side
        if y1 == y2 and x1 != x2:
            side = abs(x1 - x2)
            for dy in [side, -side]:
                p3 = (x1, y1 + dy)
                p4 = (x2, y2 + dy)
                if p3 in points and p4 in points:
                    squares.add(frozenset([p1, p2, p3, p4]))

        # Vertical side
        if x1 == x2 and y1 != y2:
            side = abs(y1 - y2)
            for dx in [side, -side]:
                p3 = (x1 + dx, y1)
                p4 = (x2 + dx, y2)
                if p3 in points and p4 in points:
                    squares.add(frozenset([p1, p2, p3, p4]))

print(len(squares))
