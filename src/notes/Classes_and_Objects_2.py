class upt:
    def __init__(self, toot):
        self._toot= toot

ghf = upt('raat')

print(ghf.__class__)

if isinstance(ghf, upt):
    print(ghf, "is of type MyClass")

