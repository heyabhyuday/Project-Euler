#Problem 52: Permuted Multiples

N, K = input().split()
N = int(N)
K = int(K)


def multipleCheck(digits, multiple):
    multiple = sorted(list(str(multiple)))
    return digits == multiple


for i in range(125874, N+1):
    flag = True
    digits = sorted(list(str(i)))

    for j in range(1, K+1):
        multiple = i*j
        if not multipleCheck(digits, multiple):
            flag = False
            break

    if flag:
        for j in range(1, K + 1):
            print(i*j, end=" ")
        print()
