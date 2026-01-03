"""
Problem:
--------
The program must accept a string S containing multiple words in lower case
as the input. The program must concatenate the words in S based on the
following conditions.

1. If two words are the same in the given string, then the program must
   concatenate those words as a single word.
2. Concatenation should be done in pairs (two at a time).
3. If a word occurs an odd number of times, the remaining word should be
   kept as it is.
4. After concatenating all possible words, the program must print the words
   in sorted order.

Boundary Conditions:
--------------------
3 <= Length of S <= 1000

Input Format:
-------------
The first line contains S (space-separated words).

Output Format:
--------------
The first line contains the words separated by a space based on the
given conditions.

Example:
--------
Input:
cat code cat code moon earth cat

Output:
cat catcat codecode earth moon
"""

words = input().split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
result = []
for word, count in freq.items():
    pairs = count // 2
    leftover = count % 2
    for _ in range(pairs):
        result.append(word * 2)
    if leftover:
        result.append(word)
print(*sorted(result))
