def n_sum1(total, lst):
    """
    >>> n_sum1(10238, [99, 199, 1999, 10000,39,1499])
    True
    >>> n_sum1(1,[1])
    True
    >>> n_sum1(5,[3,2,1])
    True
    >>> n_sum1(5,[2,1,1,6])
    False
    """
    return n_sum(total, sorted(lst))

def n_sum(total, lst):
    
    
    
    if total > sum(lst):
        return False
    elif len(lst) == 1 and total == lst[0]:
        return True
    elif len(lst) == 1 and total != lst[0]:
        return False 
    elif len(lst) == 0:
        return False
    else:
        return n_sum(total-lst[0], lst[1:]) or n_sum(total, lst[1:])

