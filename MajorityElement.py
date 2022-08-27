
# You are reading a sequence of strings. You know a priori thatmore than half the strings are repetitions of a single 
# string (the "majority element") but the positions where the majority element occurs are unknown. 
# Write a program that makes a single pass over the sequence and identifies the majority element. 
# For example, if the input is <b,a,c,A,a,b,a,a,c,a>, then a is the majority element 
# (it appears in 6 out of the 10 places). 


# Solution: Explanation. We will imagine that there are two subgroups, one containing the majority element,
# The other doesn't. We know that m/n > 1/2, where m is the majority element and n is the number of element.
# The trick here is, at most one of the two distinct entries can be the majority element, if they're different. 
# Therefore if we remove both of them, the ratio of the majority element remained unchanged, m - 1 / n - 1 > 1 / 2.
# The other case is that if we remove both of them, and they both weren't the majority element, then the majority
# element candidate remains the same, m / n - 2 > 1 / 2.

def MajorityElement(char_arr):
	maj_count = 1
	candidate = char_arr[0]
	for i in range(1, len(char_arr)):
		if maj_count == 0:
			candidate = char_arr[i]
			maj_count += 1
		cur_letter = char_arr[i]
		if cur_letter == candidate:
			maj_count += 1
		else:
			maj_count -= 1

	return candidate