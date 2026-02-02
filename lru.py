"""
Problem:
LRU - Number of Pages Added

The program must accept N integers representing the N page requests and the size S of an LRU (Least Recently Used) cache as input. After R requests, the size of the LRU cache is increased by X. The values of R and X are also passed as input. The program must print the number of pages added to the cache when processing the N requests.

Boundary Conditions:
1 <= R < N <= 1000  
1 <= Each integer value <= 1000  
1 <= S, X <= 100  

Input Format:
The first line contains N.  
The second line contains N integer values separated by a space.  
The third line contains S, R and X separated by a space.

Output Format:
The first line contains the number of pages added to the cache when processing the N requests.

Example Input:
12  
1 2 1 3 1 4 5 1 2 6 3 2  
3 4 2

Example Output:
7
"""

n = int(input())
pages = list(map(int, input().split()))
s, r, x = map(int, input().split())

cache = []
added = 0

for i in range(n):
    page = pages[i]
    if page in cache:
        cache.remove(page)
        cache.insert(0, page)
    else:
        if len(cache) < s:
            cache.insert(0, page)
        else:
            cache.pop()
            cache.insert(0, page)
        added += 1
    if i + 1 == r:
        s += x

print(added)
