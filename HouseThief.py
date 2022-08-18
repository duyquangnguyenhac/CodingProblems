# There are n houses built in a line. A thief wants to steal the maximum possible 
# money from these houses. The only restriction the thief has is that he can’t steal 
# from two consecutive houses, as that would alert the security system. How 
# should the thief maximize his stealing?

def HouseThief(houseArr):
	n = len(houseArr) + 2
	dp = [0 for _ in range(n)]
	for i in range(2, n):
		dp[i] = max(dp[i - 1], dp[i - 2] + houseArr[i - 2])
	return dp[n - 1]
	
if __name__ == '__main__':
	testA = [2, 5, 1, 3, 6, 2, 4]
	testB = [2, 10, 14, 8, 1]
	print(HouseThief(testA))
	print(HouseThief(testB))
