# We are given a ribbon of length ‘n’ and a set of possible ribbon lengths. 
# We need to cut the ribbon into the maximum number of pieces that comply 
# with the above-mentioned possible lengths. Write a method that will 
# return the count of pieces.

# Unbounded Knapsack
import math

def rodCutting(n, ribbons):
	rows = len(ribbons)
	cols = n + 1
	dp = [[-math.inf for _ in range(cols)] for _ in range(rows)]
	for i in range(rows):
		dp[i][0] = 0
	for i in range(rows):
		for j in range(1, cols):
			curCut = ribbons[i]
			includeTheCut = -1
			excludeTheCut = -1
			if i > 0:
				excludeTheCut = dp[i - 1][j]
			if j >= curCut and dp[i][j - curCut] != -math.inf:
				includeTheCut = dp[i][j - curCut] + 1
			dp[i][j] = max(excludeTheCut, includeTheCut)
	return dp[rows - 1][n]

if __name__ == '__main__':
	testA = (5, [2, 3, 5])
	testB = (7, [2, 3])
	testC = (13, [3, 5, 7])

	print(rodCutting(testA[0], testA[1]))
	print(rodCutting(testB[0], testB[1]))
	print(rodCutting(testC[0], testC[1]))
