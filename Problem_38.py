#Problem 38: Pandigital Multiples

N, K = input().split()
N = int(N)
K = int(K)

checkstr = "12345678"
if K == 9: checkstr = "123456789"

muls = []

def listtostr(ls):
    st = ""
    for e in sorted(ls):
        st += e
    return st

for i in range(2, N):
    tempstr = ""
    for j in range(1, 10):
        tempstr += str(i * j)
        if len(tempstr) != K:
            continue
        if listtostr(tempstr) == checkstr:
            print(i)
