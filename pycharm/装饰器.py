class MyClass:
    @staticmethod
    def smeth():
        print('this is a static method')

    @classmethod
    def cmeth(cls):
        print('this is a class method of', cls)


print(MyClass.smeth())
print(MyClass.cmeth())
