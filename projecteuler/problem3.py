"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

""" find prime factors via sieve of eratosthenes
    http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    
"""
def prime(n):
    
    primes = []
    if n % 2 == 0:
        primes.append(2)
         
    primes += ([i for i in range(3, int(math.sqrt(n)), 2) if n % i == 0])
    
    for i in range(3, int(math.sqrt(n))):
        for k, j in enumerate(primes):
            if j != i and j % i == 0:
                del primes[k]

    return primes
def prime2(n): 
    start = int(math.sqrt(n))
    index = start if start % 2 != 0 else start -1

    for i in range(index, 2, -2):
        if n % i == 0:
            right = True
            for j in range(3, start, 2):
                if j != i and i % j == 0:
                    right = False
                    break
            if right == True: return i
            
    if n % 2 == 0: return 2
    return 1
        
def version1():
    print prime(600851475143)[-1]

def version2():
    print prime2(600851475143)
    
    
version2()

