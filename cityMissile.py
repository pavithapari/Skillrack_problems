"""Problem:
There are N cities arranged in a row and each city has a missile that will destroy another city to its left or right. The program must accept N pairs of integers (X, Y) as the input. The value of X indicates the position of a city. The value of Y indicates the number of positions that the missile can travel. The sign of Y indicates the direction in which the missile can travel. The program must print "YES" if there are any two cities which can destroy each other. Else the program must print "NO" as the output.
Boundary Condition(s):
2 <= N <= 1000
-1000 <= X <= 1000
-1000 <= Y <= 1000 (where Y != 0)
Input Format:
The first line contains N.
The next N lines, each contains 2 integers X and Y separated by a space.
Output Format:
The first line contains YES or NO.
Example Input/Output 1:
Input:
2
3 2
5 -2
Output:
YES"""
n = int(input())
cities = [tuple(map(int, input().split())) for _ in range(n)]

found = False
for i in range(n):
    x1, y1 = cities[i]
    target1 = x1 + y1
    for j in range(n):
        if i == j: 
            continue
        x2, y2 = cities[j]
        target2 = x2 + y2
        if target1 == x2 and target2 == x1:
            found = True
            break
    if found:
        break

print("YES" if found else "NO")
