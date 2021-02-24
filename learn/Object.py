class person:

    def set_name(self,name):
        self.name=name

    def get_name(self):
        return self.name

    def greet(self):
        print("hello,world! i'm {}.".format(self.name))

foo = person()
bar = person()
foo.set_name('yang')
bar.set_name('wen')

