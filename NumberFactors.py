

# Given a number ‘n’, implement a method to count how many possible ways there are to express ‘n’ as the sum of 1, 3, or 4.

def numOfWays(n):
	if n == 0: return 0
	if n == 1: return 1
	if n == 2: return 1

	dp = [0 for _ in range(n + 1)]
	dp[0] = 1
	dp[1] = 1
	dp[2] = 1
	dp[3] = 2
	for i in range(4, n + 1):
		dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 4]
	return dp[n]

if __name__ == '__main__':
	testA = 3
	testB = 4
	testC = 5
	print(numOfWays(testA))
	print(numOfWays(testB))
	print(numOfWays(testC))


