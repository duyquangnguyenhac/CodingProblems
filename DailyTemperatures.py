# Given an array of integers temperatures represents the daily temperatures, return an array answer 
# such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.


# Solution: Keep a decreasing monotonic stack. These represent days that have yet to find a warmer day. If we find
# a day warmer then the top of the stack. We begin popping from the stack until cur_temp <= stack[-1]. As we pop from 
# the stack, we will calculate the current index - the index of the popped day, this will return the days needed to wait
# until a warmer day comes. 

def DailyTemperatures(arr):
	stack = []
	ans_arr = [0 for _ in range(len(arr))]
	for i in range(len(arr)):
		cur_temp = arr[i]
		while len(stack) != 0 and cur_temp > arr[stack[-1]]:
			prev_day = stack.pop()
			ans_arr[prev_day] = i - prev_day
		if len(stack) == 0:
			stack.append(i)
		elif cur_temp <= arr[stack[-1]]:
			stack.append(i)
	return ans_arr

if __name__ == '__main__':
	testA = [73,74,75,71,69,72,76,73]
	testB = [30,40,50,60]
	testC = [30,60,90]
	print(DailyTemperatures(testA))
	print(DailyTemperatures(testB))
	print(DailyTemperatures(testC))