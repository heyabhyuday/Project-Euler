#Problem 47: Distinct Prime Factors
import sys
UPPER = 2 * (10 ** 6)

def primefacts(num):
    facts = [0] * (num + 1)
    for f in range(2, num + 1):
        if facts[f]:
            continue
        for i in range(f, num + 1, f):
            facts[i] += 1
    return facts

def compute():
    n, k = input().split()
    n, k = int(n), int(k)
    pfacts = primefacts(UPPER)
    for i in range(1, n+1):
        flag = False
        if pfacts[i] == k:
            for j in range(k):
                if pfacts[i] == pfacts[i + j]:
                    flag = True
                else:
                    flag = False
                    break
        if flag:
            print(i)
            i += k


# pf = primefacts(140)
# print(pf[130:140])
compute()
