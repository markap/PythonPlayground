"""
n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def factorial(n):
    if (n == 0) : return 1
    return n * factorial(n-1)
 
print sum([int(i) for i in str(factorial(100))])

""" as one liner """
print sum([int(i) for i in str(reduce(lambda x, y: x * y, range(1, 100)))])
