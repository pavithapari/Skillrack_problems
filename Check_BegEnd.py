"""Problem:
The program must accept a string S containing multiple words as the input. The program must print "YES" if each word (except the first word) is formed from the previous word by adding exactly one character to the beginning or the end of the previous word. Else the program must print "NO" as the output.

Boundary Conditions:
4 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format:
The first line contains YES or NO.

Example Input/Output 1:
Input:
an and cand candl candle

Output:
YES

Explanation:
Here S = "an and cand candl candle".
2nd word: and (an + d)
3rd word: cand (c + and)
4th word: candl (cand + l)
5th word: candle (candl + e)
So YES is printed as the output.

Example Input/Output 2:
Input:
go god good goody

Output:
NO

Explanation:
"god" is formed from "go" by adding 'd' → valid.
"good" is formed from "god" by adding 'o' → valid.
"goody" is formed from "good" by adding 'y' → valid.
But "good" is not formed by adding exactly one character to "god" at the beginning or end (it adds 'o' in the middle), so the output is NO."""

words = input().split()

for i in range(1, len(words)):
    prev = words[i-1]
    curr = words[i]
    if not (curr[1:] == prev or curr[:-1] == prev):
        print("NO")
        break
else:
    print("YES")
