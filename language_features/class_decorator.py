"""
 a decorator example for a class method and the usage of self
 """

def title(t):
    def _mydecorator(function):
        def __mydecorator(self, *args, **kw):
            # do some stuff before the real
            # function gets called 
            if self.title == 3:
                print "foo"
            print t
            res = function(self, *args, **kw)
            # do some stuff after
            return res
        # returns the sub-function
        return __mydecorator
    return _mydecorator


class User(object):
    def __init__(self, title):
        self.title = title
    
    @title("mister")
    def p(self):
        print "user"
        
        
u = User(3)
u.p()
        
