# def counting(n):
#     for i in range(0,n):
#         yield n

def fun(m):
    for i in range(m):
        yield i**2 

# call the generator function
for n in fun(5):
    print(n)

def square(numbers):
    for n in numbers:
        yield n**2

# for n in square(100):
#     print(n)

sq = square(range(100))
for n in sq:
    print(n)