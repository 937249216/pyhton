def check_index(key):

    if not isinstance(key,int): raise TypeError
    if key < 0 : raise IndexError

class ArithmeticSequence:

    def __init__(self,start=0,step=0):
        self.start = start
        set.step=step
        self.changed = {}

    def __getattribute__(self,key):
        check_index(key)
        try : return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem_(self,key,value):
        check_index(key)
        self.changed[key]=value            
