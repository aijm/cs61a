def split(n):
    return n // 10, n % 10

# def statement header
def sum_digits(n):
    """Recursion to get the sum of digits of N
    
    >>> sum_digits(238)
    13
    >>> sum_digits(10)
    1
    >>> sum_digits(0)
    0
    """
    assert type(n) == int and n >=0, 'n must be a nonnegative integer.'
    # base case
    if n < 10:
        return n
    all_but_last, last = split(n)
    return last + sum_digits(all_but_last) # recursive call



# def luhn_sum(n):
#     """Return the result of luhn algorithm for n.
    
#     >>> luhn_sum(138743)
#     30
#     """

#     i, sum = 0, 0
#     while n > 0:
#         n, last = n // 10, n % 10
#         if i % 2:
#             sum += (last * 2) % 9
#         else:
#             sum += last
#         i += 1
    
#     return sum

def luhn_sum(n):
    """Return the result of luhn algorithm for n.
    
    >>> luhn_sum(138743)
    30
    """
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = n // 10, n % 10
    last_digit = (2 * last) % 9
    if n < 10:
        return last_digit
    return luhn_sum(all_but_last) + last_digit


def sum_digits_iter(n):
    digit_sum = 0
    while n > 0:
        n, last = split(n)
        digit_sum += last
    return digit_sum

def sum_digits_rec(n, digit_sum):
    if n == 0:
        return digit_sum
    else:
        n, last = split(n)
        return sum_digits_rec(n, digit_sum + last)


def fib(n):
    """Return Nth fibnacci number, recursive version"""
    assert type(n) == int and n > 0, 'n must be a positive integer.'
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib_iter(n):
    """Return Nth fibnacci number, iterative version"""
    assert type(n) == int and n > 0, 'n must be a positive integer.'
    # n == 1 loop 0 times
    curr = 0
    next = 1
    i = 1
    while i < n: # to compute n, need to loop n-1 times
        curr, next = next, curr + next
        i = i + 1
    
    return curr

    