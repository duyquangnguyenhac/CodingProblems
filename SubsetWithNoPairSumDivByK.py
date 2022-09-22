# Given an array of integer numbers, we need to find maximum size of a subset such that sum of each pair of this subset is not divisible by K. 


def non_divisible_subset(arr, k):
	f = [0 for _ in range(k)]

	for i in range(len(arr)):
		f[arr[i] % k] += 1

	if (k % 2 == 0):
		f[k//2] = min(f[k//2], 1)

	res = min(f[0], 1)

	for i in range(1, (k + 1) // 2):
		res += max(f[i], f[k - i])

	return res


if __name__ == '__main__':
	testA = [3, 7, 2, 9, 1]
	S1 = 3
	testB = [3, 17, 12, 9, 11, 15]
	S2 = 5
	print(non_divisible_subset(testA, S1))
	print(non_divisible_subset(testB, S2))