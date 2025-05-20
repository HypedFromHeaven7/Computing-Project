"""
A module to investigate namespaces and scope.
C Paterson 30/9/2013
"""

a = "coffee"
b = "cake"

def func1():
    a = "drunk"
    b = "eaten"
    return a, b

def func2(a, b):
    a = "drunk"
    b = "eaten"
    return a, b

def func3():
    c = a
    return c

def func4():
    global a
    a = "drunk"
    b = "eaten"
    return a, b

def func5():
    a = "drunk"
    return locals()

def func6():
    a = "empty"
    return globals()

__all__ = ['func1','func2','func3','func4','func5','func6']
