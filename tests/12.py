from operator import add
def tree(label, branches=[]):
    """construct tree by label and branches consists of tree"""
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    """get label"""
    return tree[0]

def branches(tree):
    """get branches"""
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    elif len(tree) == 1:
        return True
    else:
        return all([is_tree(x) for x in branches(tree)])

def is_leaf(tree):
    return not branches(tree)


def fib_tree(n):
    if n <= 1:
        return tree(n)
    left, right = fib_tree(n - 2), fib_tree(n - 1)
    return tree(label(left) + label(right), [left, right])

def count_leaves(tree):
    """count the numbers of leaf"""
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)

def leaves(t):
    """Return a list of leaf labels"""
    if is_leaf(t):
        return t
    else:
        branch_leaves = [leaves(b) for b in branches(t)]
        return sum(branch_leaves,[]) # sum(iterable[,start]) defalut start is 0, so we need to change it to []
        # return reduce(add, branch_leaves, [])
        # result = []
        # for x in branch_leaves:
        #     result = result + x
        # return result

def reduce(combiner, lst, base):
    """apply combiner to combine the whole elements of lst, with extra base"""
    for x in lst:
        base = combiner(base, x)
    return base

def increment_leaves(t):
    """"Return a tree like t but with leaf labels incremented"""
    if is_leaf(t):
        return [label(t) + 1]
    else:
        return tree(label(t), [increment_leaves(b) for b in branches(t)])


def print_tree(t, indent = 0):
    print(' ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)
    

def make_withdraw(balance):
    
    def withdraw(amount):
        nonlocal balance    # 希望每调用一次，balance的值可以改变
        if amount > balance:
            return 'Insufficient funds'
        else:
            balance = balance - amount
            return balance
    return withdraw