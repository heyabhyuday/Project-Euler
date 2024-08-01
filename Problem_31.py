#Problem 31: Coin Sums
coins = [1, 2, 5, 10, 20, 50, 100, 200]
all_ways = [1] + [0]*100000
mod = (10 ** 9) + 7

for coin in coins:
    for i in range(coin, len(all_ways)):
        all_ways[i] += all_ways[i - coin]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(all_ways[n] % mod)
