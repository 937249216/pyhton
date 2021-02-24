def digui(n):
    if n ==1: 
        return 1
    else:
        return n*digui(n-1)
    pass
print ('{}'.format(digui(5)))    
