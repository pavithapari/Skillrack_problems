"""Problem:
Given a list of integers, your task is to remove duplicates, sort the list, and group consecutive numbers into ranges. Each range should be printed in the format "start-end". If a number is not part of a consecutive sequence, it should still be printed as "x-x".

Boundary Conditions:
- 1 ≤ n ≤ 10^5
- Each integer in the list is between -10^9 and 10^9

Input Format:
- The first line contains an integer n, the number of elements in the list.
- The second line contains n space-separated integers.

Output Format:
- Print the ranges of consecutive numbers in ascending order, separated by a space.
- Each range should be in the format "start-end".

Example:
Input:
5
15 10 12 12 12

Output:
10-10 12-12 15-15"""

n=int(input())
lis=map(int,input().split())
lis=list(set(lis))
lis.sort()
start=lis[0]
end=lis[0]
for i in range(1,len(lis)):
  if lis[i]==end+1:
    end=lis[i]
  else:
    res.append([start,end])
    start=end=lis[i]
res.append([start,end])
for s,e in res:
  print(f"{s}-{e}",end=" ")
