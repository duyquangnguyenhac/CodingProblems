# Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.
def minimumDifference(nums):
    cumulativeSum = 0
    for num in nums:
        cumulativeSum += num
    targetSum = cumulativeSum // 2
    cols = targetSum + 1
    rows = len(nums)
    dp = [[False for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        dp[i][0] = True
    for j in range(cols):
        if j == nums[0]:
            dp[0][j] = True
    for curSum in range(cols):
        for curIndex in range(1, rows):
            curNum = nums[curIndex]
            if dp[curIndex - 1][curSum]:
                dp[curIndex][curSum] = dp[curIndex - 1][curSum]
            if curNum <= curSum:
                dp[curIndex][curSum] = dp[curIndex - 1][curSum - curNum]
    closestSum = -1
    for curSum in range(cols - 1, -1, -1):
        lastRowIdx = rows - 1
        if dp[lastRowIdx][curSum]:
            closestSum = curSum
            break
    return abs((cumulativeSum - closestSum) - closestSum)
        
if __name__ == '__main__':
	testA = [1, 2, 3, 9]
	testB = [1, 2, 7, 1, 5]
	testC = [1, 3, 100, 4]
	print(minimumDifference(testA))
	print(minimumDifference(testB))
	print(minimumDifference(testC))
