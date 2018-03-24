#!/usr/bin/env python3

# Multiples of 3 and 5
#
# If we list all the natual numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.
#
# Find the sum of all multiples of 3 or 5 below 1000.

def findMultiples(number, maximum):
	multiples = []
	for i in range(1, maximum):
		if i % number == 0:
			multiples.append(i)
	return multiples


def main():
	multiplesOf3 = findMultiples(3, 1000)
	multiplesOf5 = findMultiples(5, 1000)
	multiplesOf3Or5 = sorted(multiplesOf3 + list(set(multiplesOf5) - set(multiplesOf3)))
	print(sum(multiplesOf3Or5))

if __name__ == '__main__':
	main()
