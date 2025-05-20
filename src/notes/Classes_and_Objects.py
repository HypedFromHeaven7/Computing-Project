class Counter:

    def __init__(self):

        self.i = 0
        self.k = 10

    def addone(self):

        self.i += 1
        self.k += 4

    def reset(self, i=0):

        self.i = i
    def minone(self):

        self.i -= 1
        self.k -= 1
    
    def __repr__(self):
        return f"(i = {self.i} , k = {self.k})"
    
    def __str__(self):
        return f"{self.i} {self.k}"





c = Counter()
d = Counter()
print("######################################################################################")
print("######################################################################################")
print("######################################################################################")
print(f"Initial values for c.i and d.i, defined above are {c.i} and {d.i} respectively")
print(f"How ever c.k and d.k are different values of the same object defined as {c.k} and {d.k}")
for i in range(0,4):
    c.addone()
    d.minone()
print("######################################################################################")
print("######################################################################################")
print(f"Using the 'addone' statement we can add to the class object c, to get {c.i} and {c.k};")
print(f"and with 'minone' we can minus from object d to get, {d.i} and {d.k}.")
print("######################################################################################")
print("######################################################################################")
print(f"Using str and repr we can formate how we want a print state of the object to look like \n i.e. print(repr(c))={repr(c)} \n and print(d)={d}  --default is (str)")
print("######################################################################################")
