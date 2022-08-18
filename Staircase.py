# Given a stair with ‘n’ steps, implement a method to count how many possible ways 
# are there to reach the top of the staircase, given that, at every step you can 
# either take 1 step, 2 steps, or 3 steps.

def stairCase(n):
	if n < 2: return 1
	if n == 2: return 2

	dp = [0 for _ in range(n + 1)]
	# dp[0] is essentially the base case for when you take a 3 step from dp[3]
	dp[0] = 1
	dp[1] = 1
	dp[2] = 2

	for i in range(3, n + 1):
		dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
	return dp[n]

if __name__ == '__main__':
	testA = 3
	testB = 4
	print(stairCase(testA))
	print(stairCase(testB))