from collections import defaultdict
permcubes = defaultdict(lambda:[])

n, k = input().split()
n, k = int(n), int(k)

for i in range(1, n):
    temp = i ** 3
    s = "".join(sorted(str(temp)))
    permcubes[s].append(i)

sols = []
for item in permcubes.items():
    if len(item[1]) == k:
        sols.append(pow(min(item[1]), 3))

sols = sorted(sols)
for sol in sols:
    print(sol)
