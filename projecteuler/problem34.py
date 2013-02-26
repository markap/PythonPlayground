"""

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.


"""


def factorial(n):
    if (n == 0) : return 1
    return n * factorial(n-1)

# 10s with dict, 35s with list
factorial_dict = dict([(str(i), factorial(i)) for i in range(0, 10)])

TOP_LIMIT = 7*factorial_dict["9"]
DOWN_LIMIT = 10


def version1():
    s=0
    
    for i in range(DOWN_LIMIT, TOP_LIMIT):
        if sum([factorial_dict[j] for j in str(i)]) == i:
            s+=i

    return s


print version1()
