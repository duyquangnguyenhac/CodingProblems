# Given a staircase with ‘n’ steps and an array of ‘n’ numbers representing the fee 
# that you have to pay if you take the step. Implement a method to calculate the 
# minimum fee required to reach the top of the staircase (beyond the top-most 
# step). At every step, you have an option to take either 1 step, 2 steps, or 3 steps. 
# You should assume that you are standing at the first step.

import math

def MinimumJumpsWithFee(n, feeArr):
	dp = [math.inf for _ in range(len(feeArr) + 1)]
	dp[0] = 0
	for i in range(1, len(feeArr) + 1):
		for j in range(1, 4):
			if i - j >= 0:
				dp[i] = min(dp[i], dp[i - j] + feeArr[i - j])
	return dp[len(feeArr)]
if __name__ == '__main__':
	testA = (6, [1,2,5,2,1,2])
	testB = (4, [2,3,4,5])
	print(MinimumJumpsWithFee(testA[0], testA[1]))
	print(MinimumJumpsWithFee(testB[0], testB[1]))