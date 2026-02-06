"""
The program must accept an integer X and N pairs as the input.
Each pair contains a string and an integer.
The program must form a string S of length X based on the following conditions:

- Initially, all the characters in the string must be hyphens.

- For each string-integer pair (string str, integer P), the program must insert
  the string str into the string S starting from the position P if the string S
  contains L hyphens starting from the position P (where L represents the length
  of string str). Else the program must not modify the string S.

Finally, the program must print the modified string S as the output.

Input Format:
The first line contains X.
The second line contains N.
The next N lines, each contains a string value str and an integer P.

Output Format:
The first line contains the string S.
"""

X = int(input().strip())
N = int(input().strip())

pairs = []
for _ in range(N):
    s, p = input().split()
    pairs.append((s, int(p)))

S = ["-"] * X

for s, p in pairs:
    start = p - 1
    L = len(s)
    if start + L <= X and all(S[i] == "-" for i in range(start, start + L)):
        for i in range(L):
            S[start + i] = s[i]

print("".join(S))
