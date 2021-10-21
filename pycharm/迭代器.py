'''
class Fibs:
    """def __init__(self):"""

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a


fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)
        break

class Fibs2:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self

'''


class TestIterator:
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value

    def __iter__(self):
        return self


ti = TestIterator()
print(list(ti))
