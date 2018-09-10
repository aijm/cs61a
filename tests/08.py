from ucb import trace
def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n // 10) # 递归之后输出
shrink = lambda n: f_then_g(print, shrink, n // 10) # 递归之前输出

@trace
def count_partitions(n, m):
    """Return The number of partitions of a positive integer n, using parts up to m.
    Example:
    count_partitions(6, 4)
    2 + 4 = 6
    1 + 1 + 4 = 6
    3 + 3 = 6
    1 + 2 + 3 = 6
    1 + 1 + 1 + 3 = 6
    2 + 2 + 2 = 6
    1 + 1 + 2 + 2 = 6
    1 + 1 + 1 + 1 + 2 = 6
    1 + 1 + 1 + 1 + 1 + 1 = 6
    return 9
    
    >>> count_partitions(6, 4)
    9
    """
    if m == 1 or n == 0: # base case
        return 1
    i, sum = 1, 0
    while i <= m:
        sum += count_partitions(n - i, min(n - i, i))
        i += 1
    return sum

    # if n == 0:
    #     return 1
    # if m == 0:
    #     return 0
    # return count_partitions(n - m, min(n - m, m)) + count_partitions(n, m - 1)


 

    

