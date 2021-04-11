'''
def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

print ( list(flatten([[[1],2],3,4,[5,[6,7]],8])) )
'''

def flatten(nested):
    try:
        try:nested +' '#将对象与字符串相加检查是否会触发typeerror 
        except TypeError:pass
        else:raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested        