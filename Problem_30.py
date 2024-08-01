#Problem 30: Digit Nth Powers
n = int(input().strip())

def digitsum(a, b):
    return sum(int(i) ** a for i in str(b))

print(str(sum(i for i in range(2, 1000000) if i == digitsum(n, i))))
