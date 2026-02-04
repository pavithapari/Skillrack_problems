n = int(input())
lis = list(map(int, input().split()))

best_len, best_sum = 0, 0
curr_len, curr_sum = 1, lis[0]
prev_last = int(str(lis[0])[-1])  
for i in range(1, n):
    curr_first = int(str(lis[i])[0])

    if curr_first == prev_last:
        curr_len += 1
        curr_sum += lis[i]
    else:
        curr_len, curr_sum = 1, lis[i]

    prev_last = int(str(lis[i])[-1])
    if curr_len >= 2:
        if curr_len > best_len or (curr_len == best_len and curr_sum > best_sum):
            best_len, best_sum = curr_len, curr_sum

if best_len < 2:
    print(max(lis))
else:
    print(best_sum)
