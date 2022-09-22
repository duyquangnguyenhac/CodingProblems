# Given a simulation of a falling figure. Remove the minimum amount of obstacles for the figure to touch the ground. Given
# that the figure is guaranteed to be one piece connected by adjacent or diagonal sides.
# Where, * -> figure, and X -> obstacle, and o is an open space.

# Ex.
# * * * 
# X * *
# * * o 
# o o o
# o X X
# Sol: 3

# Ex.
# * * * 
# * o *
# * X * 
# o X o
# o X X


# k = 0 -> 4. Count 2 x 2 submatrices containing 0 to 4 black elements. Given # of row, and index.
