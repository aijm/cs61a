counts = [1, 2, 3]
sum = 0
for x in counts:
    sum += x
print('sum:', sum)
# equals to 

items = iter(counts)
sum_iter = 0
while True:
    try:
        item = next(items)
        sum_iter += item
    except StopIteration as e:
        break
print('sum_iter:', sum_iter)


def contains(a, b):
    """Return whether sequence A contains all the elements of B in order.
    >>> contains('strength', 'stent')
    True
    >>> contains('strength', 'rest')
    False
    >>> contains('strength', 'tenth')
    True
    """
    i, j = 0, 0
    while i < len(a) and j < len(b):
        while a[i] != b[j]:
            i += 1
            if i == len(a):
                break
        j += 1
        i += 1
    if j == len(b):
        return True
    else:
        return False

def contains_iter(a, b):
    """Return whether sequence A contains all the elements of B in order.
    >>> contains_iter('strength', 'stent')
    True
    >>> contains_iter('strength', 'rest')
    False
    >>> contains_iter('strength', 'tenth')
    True
    """
    ai = iter(a)
    for x in b:
        try:
            while next(ai) != x:
                pass
        except StopIteration:
            return False
    return True



def double(x):
    print('**', x, '=>', 2*x, '**')
    return 2*x


def evens(start, end):
    """Generator of evens between start and end."""
    even = start + start % 2
    while even < end:
        yield even
        even += 2

            
        
    


