""" Optional problems for Lab 3 """

from lab03 import *

## Higher order functions

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    compose1 = lambda f, g: lambda x: f(g(x)) # compose f(x),g(x) to f(g(x))
    def cycle_by_n(n): # using recursion n ---> n - 1 
        if n == 0:
            return lambda x: x
        elif n % 3 == 0:
            return compose1(f3, cycle_by_n(n - 1))
        elif n % 3 == 1:
            return compose1(f1, cycle_by_n(n - 1))
        else:
            return compose1(f2, cycle_by_n(n - 1))
    
    return cycle_by_n
        





## Lambda expressions

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: y * 10 + x % 10
    while x > 0:
        x, y = x // 10, f() # x 每次移除最后一位，y将移除的那一位往后添加，得到n的逆序
    return y == n

## More recursion practice

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return n * skip_mul(n - 2)

def is_prime(n, i = 3):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    # iterative version
    # if n == 2:
    #     return True
    # elif n <= 1 or n % 2 == 0:
    #     return False
    # else:
    #     i, end = 3, int(n ** 0.5)
    #     while i <= end:
    #         if n % i == 0:
    #             return False
    #         i += 2
    #     return True
    if n == 2:
        return True
    elif n <=1 or n % 2 == 0:
        return False
    elif n % i == 0:
        return False
    elif i * i > n:
        return True
    else:
        return is_prime(n, i + 2)

    


def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    
    


    

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0
    return ten_pairs(n // 10) + count_digit_rec(n // 10, 10 - n % 10)

def count_digit(n, d):
    count = 0
    while n > 0:
        n, last = n // 10, n % 10
        if last == d:
            count = count + 1
    return count

def count_digit_rec(n, d):
    if n < 10:
        return 1 if n == d else 0
    else:
        return count_digit_rec(n // 10, d) + count_digit_rec(n % 10, d)



