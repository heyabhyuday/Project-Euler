#Problem 13: Large Sum
nums = []

N = int(input().strip())
for i in range(N):
    nums.append(int(input().strip()))

print(str(sum(nums))[:10])

