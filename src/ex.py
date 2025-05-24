import some_module as sm

a=sm.MyClass(4)

# The instance variable should be 4
a.inst_var
4

# When the instance a was initialised the class variable was incremented.
sm.MyClass.class_var
1

# Note we can access the class_var through instance a.
# This is discouraged however as it could be overridden by an
# instance variable with the same name
a.class_var
1

# Let's create more
b=sm.MyClass(5)

c=sm.MyClass(4.3)

# The instance variables should be 5 & 4.3
b.inst_var
5
c.inst_var
4.3

# The class variable will be incremented for each instance initialisation.
sm.MyClass.class_var
3

# Likewise we can (but probably should not) access them through the
# instances a, b & c
a.class_var
3

b.class_var
3

c.class_var
3