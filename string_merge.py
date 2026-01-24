"""Problem:
--------
The program must accept a string S containing multiple words in lower case
as the input. The program must concatenate the words in S based on the
following conditions.

1. The words must be merged in sequence from left to right.
2. When concatenating two adjacent words, the program must remove the
   maximum overlapping part where the ending characters of the first word
   match the starting characters of the next word.
3. If no such overlap exists, the two words must be concatenated directly.
4. The final merged string must be printed as the output.

Boundary Conditions:
--------------------
2 <= Number of words in S <= 100
1 <= Length of each word <= 100

Input Format:
-------------
The first line contains S (space-separated words).

Output Format:
--------------
The first line contains the merged string based on the given conditions.

Example:
--------
Input:
water terminator ortho

Output:
waterminatortho

Input:
ababab ababab bababa bababa

Output:
abababababa
"""

def merge(res,word):
  max_overlap=min(len(res),len(word))
  for i in range(max_overlap,0,-1):
    if res[-i:]==word[:i]:
      return res+word[i:]
  return res+word
lis=input().strip().split()
res=lis[0]
for i in lis[1:]:
  res=merge(res,i)
print(res)
  

