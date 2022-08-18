# Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.
# You can only use each number once.

def CountOfSubsetSum(numberArr, S):
	rows = len(numberArr)
	cols = S + 1
	dp = [[0 for _ in range(cols)] for _ in range(rows)]
	for i in range(rows):
		dp[i][0] = 1
	for j in range(cols):
		if numberArr[0] == j:
			dp[0][j] = 1
	for curSum in range(cols):
		for curIdx in range(1, rows):
			curNum = numberArr[curIdx]
			if dp[curIdx - 1][curSum] > 0:
				dp[curIdx][curSum] += dp[curIdx - 1][curSum]
			dp[curIdx][curSum] += dp[curIdx - 1][curSum - curNum]
	return dp[len(numberArr) - 1][S]

if __name__ == '__main__':
	testA = [1, 1, 2, 3]
	S1 = 4
	testB = [1, 2, 7, 1, 5]
	S2 = 9
	print(CountOfSubsetSum(testA, S1))
	print(CountOfSubsetSum(testB, S2))
