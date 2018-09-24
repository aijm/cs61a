from operator import add, mul

def reduce(f, s, initial):
    """Combine elements of s using f starting with initial 

    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(add, [1, 2, 3, 4], 0)
    10
    """
    for x in s:
        initial = f(initial, x)
    return initial