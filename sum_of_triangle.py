"""Problem:
--------
A matrix having (N+1)/2 rows and N columns (where N is odd) is passed as the input. 
A triangle with non-zero values is present in the middle of the matrix. 
The program must print the sum of the values in the boundary of the triangle.

Boundary Conditions:
--------------------
5 <= N <= 49

Input Format:
-------------
The first line contains N.
The next (N+1)/2 lines, each contains N integer values separated by a space.

Output Format:
--------------
The first line contains the sum of integer values in the boundary of the triangle.

Example:
--------
Input:
5
0 0 1 0 0
0 6 5 2 0
3 5 4 9 8

Output:
38

Explanation:
The integer values along the boundary are 1, 2, 8, 9, 4, 5, 3 and 6.
Their sum is 38, which is printed as the output.

Input:
7
0 0 0 3 0 0 0
0 0 9 4 8 0 0
0 8 6 7 9 5 0
1 4 4 8 5 7 1

Output:
63"""

n=int(input())
r=(n+1)//2
lis=[]
for i in range(r):
  lis.append(list(map(int,input().split())))
sum_=0
j=r-1
for i in range(r):
  if(i==0):
    sum_+=lis[i][j]
  elif (i==(r-1)):
    sum_+=sum(lis[i])
  else:
    sum_+=lis[i][j]+lis[i][-(j+1)]
  j-=1
print(sum_)
