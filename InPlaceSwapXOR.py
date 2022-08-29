# Given variable x, y. Swap in place without using any helper variables.


def InPlaceSwap(x, y):
	x ^= y # (x^y, y)
	y ^= x # (x^y, y^x^y)
	x ^= y # (x^y^y^x^y, y^x^y) => (y, x)
	return x, y

if __name__ == '__main__':
	x, y = 2, 3
	print(InPlaceSwap(x, y))