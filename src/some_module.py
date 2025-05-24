class MyClass:
    # no need for dot notation
    class_var = 0

    def __init__(self, vv):
        self.inst_var = vv       # now need the dot notation
        MyClass.class_var += 1   # note that it is of MyClass not self