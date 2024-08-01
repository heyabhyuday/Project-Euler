#Problem 24: Lexicographic Permutations
import sys
string = 'abcdefghijklm'

facts = [1]
for i in range(1, 14):
    facts.append(facts[i-1] * i)

t = int(input().strip())
for a0 in range(t):
    n =int(input().strip())
    stl = list(string)
    perm = ''
    c = 0
    k = 1
    while k < 14:
        for i in range(len(stl)):
            if c + facts[13-k] >= n:
                perm += stl[i]
                del(stl[i])
                k += 1
                break
            c += facts[13-k]
    print(perm)
