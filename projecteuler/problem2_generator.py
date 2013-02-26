""" eulers problem 2 but now with a generator for the fibonacci function
"""


def fib():
    a,b = 0,1
     
    while True:
        yield a
        a,b = b,a+b  
  

f = fib()  
l = []     
while True:
    n = f.next() 
    if n > 4000000:
        break
    if n % 2 == 0:
        l.append(n)
    
print sum(l)
