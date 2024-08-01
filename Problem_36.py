#Problem 36: Double-base Palindromes
import sys

def baseswitch(num, base):
    new_num = ""
    while num > 0:
        digit = num % base
        if digit < 10:
            new_num += str(digit)
        else:
            new_num += str(ord('A') + digit-10)
        num //= base
    new_num = new_num[::-1]
    return new_num

def doublepal(num, base):
    if str(num) != str(num)[::-1]:
        return False
    new_num = baseswitch(num, base)
    return str(new_num) == str(new_num)[::-1]

def sumtillN(num, base):
    return sum(i for i in range(1, num) if doublepal(i, base))

N, K = input().split()
N, K = int(N), int(K)
print(sumtillN(N, K))
