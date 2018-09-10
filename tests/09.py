from ucb import trace

@trace
def gcd(m, n):
    """Return the largest k that divides both m and n

    >>> gcd(4, 6)
    2
    >>> gcd(1, 10)
    1
    >>> gcd(2, 18)
    2
    >>> gcd(18, 12)
    6
    """
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

# funciton currying
# equal to curry2 = lambda f: lambda x: lambda y: f(x, y)
def curry2(f): 
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g


def trace1(fn):
    """Return a function(one argumment) with calling information."""
    def traced(x):
        print('Calling', fn, 'with argumment', x)
        return fn(x)
    return traced


# @trace1
def square(x):
    return x * x
square = trace1(square)

def sum_squares_up_to(n):
    k, total = 1, 0
    while k <= n:
        total, k = total + square(k), k + 1
    return total