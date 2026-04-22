
import math


def magic_fibonacci(n):
	'''Returns the nth Fibonacci number using division.'''
	digits = int(input("Enter the number of fibonacci numbers to generate: "))
	n = 1 / 89
	p = n * (10 ** digits)
	return int(p)

def extract_digits_from_fraction(n, i, j):
	# Remove the digits before index i
	t = n * (10 ** i)
	fp, _ = math.modf(t)
	# Remove the digits after index j
	u = fp * (10 ** (j - i + 1))
	f = int(u)
	return f

for n in [2.34567093884, 8.765342322, 23.011234832]:
	print(extract_digits_from_fraction(n=n, i=3, j=6), n)
