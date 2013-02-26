


def sample_fn(*args):
    for i in args:
        print i
    

sample_fn("first", "second", "third")

def sample_fn2(**kwargs):
    for k, w in kwargs.items():
        print k + " -> " + str(w)
    
sample_fn2(name="Martin", age=23)


class Kwargs(object):       
    def __init__(self, **kwargs):
        acceptable_keys_list = ['name', 'age']
        
        for k in kwargs.keys():
            if k in acceptable_keys_list:
                self.__setattr__(k, kwargs[k])
                
k = Kwargs(age=21, name="Martin", foo="bar")
print k.__dict__