

def foo(function):
        def __mydecorator(*args, **kw):
            # do some stuff before the real
            # function gets called 
            print args
            res = function(*args, **kw)
            print res
            # do some stuff after
            return res
        # returns the sub-function
        return __mydecorator
    
    
def multiply(n, m):
    def _mydecorator(function):
        def __mydecorator(*args, **kw):
            # do some stuff before the real
            # function gets called 
            res = function(args[0] * n, args[1] * m, **kw)
            # do some stuff after
            return res
        # returns the sub-function
        return __mydecorator
    return _mydecorator


@multiply(2,3)
def p(n, m):
    return n, m

print p(3,3)