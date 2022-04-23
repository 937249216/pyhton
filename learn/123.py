'''
print(format("Ursula"," >20"))    
print(format("Ursula"," ^20"))   
print(format("Ursula"," <20"))'''


class counterlist(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super(counterlist, self).__getitem__(index)


cl = counterlist(range(10))
print(cl)
