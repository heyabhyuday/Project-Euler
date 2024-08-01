N = int(input().strip())
Triangles = []

for a0 in range(N):
    temp = tuple(map(int, input().split()))
    Triangles.append(temp)


def check_origin(x1, y1, x2, y2, x3, y3):
    a = sign((y1 - y2) * x1 - (x1 - x2) * y1)
    b = sign((y2 - y3) * x2 - (x2 - x3) * y2)
    c = sign((y3 - y1) * x3 - (x3 - x1) * y3)
    return 0 in (a, b, c) or a == b == c


def sign(x):
    if x > 0: return 1
    elif x < 0: return -1
    else: return 0


print(sum(1 for triangle in Triangles if check_origin(*triangle)))
