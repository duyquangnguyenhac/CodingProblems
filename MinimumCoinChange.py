# Given an infinite supply of ‘n’ coin denominations and a total money amount, we 
# are asked to find the minimum number of coins needed to make up that amount

import math

def MinimumCoinChange(coins, k):
	dp = [math.inf for _ in range(k + 1)]
	dp[0] = 0

	for i in range(1, k + 1):
		for j in range(len(coins)):
			if coins[j] <= i:
				dp[i] = min(dp[i], dp[i - coins[j]] + 1)
	return dp[k]

if __name__ == '__main__':
	testA = [1, 2, 5]
	S1 = 11
	testB = [9, 6, 5, 1]
	S2 = 11
	print(MinimumCoinChange(testA, S1))
	print(MinimumCoinChange(testB, S2))