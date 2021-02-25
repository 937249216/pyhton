

class MuffledCalculator:
    muffled = False
    def calc(self,expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('division by zero is illegal')
            else:
                raise    
    
calculator = MuffledCalculator()
calculator.muffled = False
calculator.calc('10/0')



