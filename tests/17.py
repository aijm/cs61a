# Representation

# String Representations
## str --> humans
## repr --> Python Interpreter


class Bear:
    """A Bear."""

    def __init__(self):
        self.__repr__ = lambda: 'oski'
        self.__str__ = lambda: 'this bear'

    def __repr__(self):
        return 'Bear()'

    def __str__(self):
        return 'Bear[]'
    
    def haha(self):
        return 'haha'

# oski = Bear()
# print(oski)
# print(str(oski))
# print(repr(oski))
# print(oski.__str__()) 
# print(oski.__repr__())
# print(type(oski))
# print(type(oski).__repr__(oski))

def repr(x):
    return type(x).__repr__(x)

def str(x):
    t = type(x)
    if hasattr(t, "__str__"):
        return t.__str__(x)
    else:
        return repr(x)


# Interface
class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d
    
    def __repr__(self):
        """Method invoked to display an object as an python expression"""
        return f'Ratio({self.numer}, {self.denom})'

    def __str__(self):
        return '{}/{}'.format(self.numer, self.denom)
    
    def __add__(self, other):
        d = self.denom * other.denom
        n = self.numer * other.denom + other.numer * self.denom
        g = gcd(n, d)
        return Ratio(n//g, d//g)


def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a % b)

def fib(n):
    current, next = 0, 1
    i = 0
    while i < n:
        current, next = next, current + next
        i += 1
    return current