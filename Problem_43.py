from itertools import permutations
divs = [2, 3, 5, 7, 11, 13, 17]
n = int(input().strip())


def isDivisible(num):
    return all((num[i + 1] * 100 + num[i + 2] * 10 + num[i + 3]) % p == 0 for (i, p) in enumerate(divs[:n-2]))


psum = sum(int(''.join(map(str,num))) for num in permutations(range(n+1)) if isDivisible(num))
print(psum)
