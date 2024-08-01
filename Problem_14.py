#Problem 14: Longest Collatz Sequence

t = int(input().strip())
n = [int(input()) for x in range(t)]
UPPER = 5 * (10 ** 6)
answer = [1 for x in range(UPPER + 1)]
result = [1 for x in range(UPPER + 1)]

for i in range(2, UPPER + 1):
    seqlen = 0
    curr = i
    while True:
        if curr < i:
            answer[i] = seqlen + answer[curr]
            break
        if curr % 2 == 0:
            seqlen += 1
            curr = curr // 2
        else:
            curr = (3 * curr + 1) // 2
            seqlen += 2

tempmax = 1
index = 1

for i in range(2, UPPER + 1):
    if answer[i] >= tempmax:
        tempmax = answer[i]
        index = i
    result[i] = index

for x in n:
    print(result[x])
