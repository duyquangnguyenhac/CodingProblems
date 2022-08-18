# Given an array of positive numbers, where each element represents the max 
# number of jumps that can be made forward from that element, write a program 
# to find the minimum number of jumps needed to reach the end of the array 
# (starting from the first element). If an element is 0, then we cannot move 
# through that element.

import math

def MinimumJumpsToTheEnd(jumpsArr):
	if jumpsArr[0] == 0:
		return -1
	n = len(jumpsArr)
	dp = [math.inf for _ in range(n)]
	dp[0] = 0
	for i in range(1, n):
		for j in range(i):
			if j + jumpsArr[j] == i:
				dp[i] = min(dp[i], dp[j] + 1)
	print(dp)
	return dp[n - 1]
	
if __name__ == '__main__':
	testA = [2, 1, 1, 1, 4]
	testB = [1, 1, 3, 6, 9, 3, 0, 1, 3]
	print(MinimumJumpsToTheEnd(testA))
	print(MinimumJumpsToTheEnd(testB))