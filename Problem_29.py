#Problem 29: Distinct Powers

N = int(input().strip())
count = 0
excheck = [False] * (N+1)
for a in range(2, N+1):
    if excheck[a]:
        continue
    combined = set()
    ex = 2
    while a ** ex <= N:
        excheck[a ** ex] = True
        temp = set([b*ex for b in range(2, N+1) if b*ex > N])
        combined.update(temp)
        ex += 1
    count += len(combined) + N-1
print(count)
