# You are given an array A of n - 1 integers which are in the range between 1 and n. [1, n]
# All numbers appear exactly once, except one number, which is missing. Find this missing number.

# Solution: Since XOR eliminate duplicates. We can XOR all numbers from 1 to n. The left over number is the missing number.


def FindingMissingElement(arr, n):
	a = 0
	for i in range(len(arr)):
		cur_num = arr[i]
		a ^= cur_num
	for j in range(1, n + 1):
		a ^= j
	return a

if __name__ == '__main__':
	testA = [1, 3, 4]
	n = 4
	print(FindingMissingElement(testA, 4))