# Given a set of positive integer numbers, find if we can partition it into two subsets
# such that the sum of elements in both subsets is equal.


def EqualSubsetSumPartition(numberArr):
	cumSum = 0
	for number in numberArr:
		cumSum += number
	if cumSum % 2 != 0:
		return False
	targetSum = cumSum // 2
	rows = len(numberArr)
	cols = targetSum + 1
	dp = [[False for _ in range(cols)] for _ in range(rows)]
	for i in range(rows):
		dp[i][0] = True
	for j in range(cols):
		if j - numberArr[0] == 0:
			dp[0][j] = True
	for curSum in range(cols):
		for numberIdx in range(1, rows):
			curNum = numberArr[numberIdx]
			if dp[numberIdx - 1][curSum]:
				dp[numberIdx][curSum] = dp[numberIdx - 1][curSum]
			elif curNum <= curSum:
				dp[numberIdx][curSum] = dp[numberIdx - 1][curSum - curNum]
	return dp[len(numberArr) - 1][targetSum]

if __name__ == '__main__':
	testA = [1, 2, 3, 4]
	testB = [1, 1, 3, 4, 7]
	testC = [2, 3, 4, 6]
	print(EqualSubsetSumPartition(testA))
	print(EqualSubsetSumPartition(testB))
	print(EqualSubsetSumPartition(testC))
