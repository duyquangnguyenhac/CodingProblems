# You are given an array A of n + 1 integers which are in the range between 1 and n. 
# All numbers appear exactly once, except one number, which is duplicated. 
# Find this duplicated number.

# Solution: If you XOR two of the same numbers, they will cancel out. If we XOR everything to 1 to n, the duplicated number
# will be XOR 3 times, and therefore will not be cancelled out.


def FindingDuplicateElement(arr, n):
	a = 0
	for i in range(1, n + 1):
		a ^= i
	for j in range(len(arr)):
		a ^= arr[j]
	return a

if __name__ == '__main__':
	testA = [1, 2, 3, 4, 5, 3]
	n = 5
	print(FindingDuplicateElement(testA, n))