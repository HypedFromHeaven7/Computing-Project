class MyClass:


    def __init__(self):

        self.public_variable = 123

        self._hidden_variable = 'abc'

        self.__mangled_variable = 'abc123'


    def some_method(self):

        # all can be accessed from within the class

        print(self.public_variable)

        print(self._hidden_variable)

        print(self.__mangled_variable)


c = MyClass()
print(f"{c._hidden_variable}\n{dir(c)}")