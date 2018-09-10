def make_adder(n):
    """Return a function that takes a 
    K and return K + N.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    
    return adder


def square(x):
    return x * x

def triple(x):
     return 3 * x

def compose1(f, g):
    def h(x):
        return f(g(x))

    return h


def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x += 1

def inverse(f):
    """Return g(y) such that g(f(x)) => x"""
    return lambda y: search(lambda x: f(x) == y)



j = 1
i = 1

while i < 3:
    k = i
    j = i
    i += 1

if j == 2:
    m = 3

print(m)
print(j)
print(k)