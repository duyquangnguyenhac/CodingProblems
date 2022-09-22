# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.


def RotateMatrix(matrix):
	l, r = 0, len(matrix) - 1
	while l < r:
		top, bottom = l, r
		for i in range(r - l):
			topLeft = matrix[top][left + i]
			matrix[top][l + i] = matrix[bottom - i][l]
			matrix[bottom - i][l] = matrix[bottom][r - i]
			matrix[bottom][r - i] = matrix[top + i][r]
			matrix[top + i][r] = topLeft
		r -= 1
		l += 1