class Tree:
    def __init__(self, label, branches=[]):
        # assert isinstance(branches, list)
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({}{})'.format(self.label, branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = [] # a list contains every line of output
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches


class BTree(Tree):
    """Binary Tree"""
    empty = Tree(None) # define empty node
    def __init__(self, label, left=empty, right=empty):
        for b in (left, right):
            assert isinstance(b, BTree) or b is BTree.empty
        super().__init__(label, [left, right])

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]

    def is_leaf(self):
        return self.left is BTree.empty and self.right is BTree.empty


    def __repr__(self):
        if self.is_leaf():
            return 'BTree({0})'.format(self.label)
        elif self.right is BTree.empty:
            left = repr(self.left)
            return 'BTree({0}, {1})'.format(self.label, left)
        else:
            left, right = repr(self.left), repr(self.right)
            if self.left is BTree.empty:
                left = 'BTree.empty' 
            template = 'BTree({0}, {1}, {2})'
            return template.format(self.label, left, right)

def fib_tree(n):
    """Fibonacci binary tree.

    >>> fib_tree(3)
    BTree(2, BTree(1), BTree(1, BTree(0), BTree(1)))
    """
    if n == 0 or n == 1:
        return BTree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.label + right.label
        return BTree(fib_n, left, right)

def contents(t):
    """The values in a binary tree.

    >>> contents(fib_tree(5))
    [1, 2, 0, 1, 1, 5, 0, 1, 1, 3, 1, 2, 0, 1, 1]
    """
    if t is BTree.empty:
        return []
    else:
        return contents(t.left) + [t.label] + contents(t.right)


def balanced_bst(s):
    """Construct a binary search tree from a sorted list."""
    if not s:
        return BTree.empty
    else:
        mid = len(s) // 2
        left = balanced_bst(s[:mid])
        right = balanced_bst(s[mid+1:])
        return BTree(s[mid], left, right)


def largest(t):
    """Return the largest element of a binary search tree.

    >>> s = [1, 2, 3, 4, 5]
    >>> bs = balanced_bst(s)
    >>> largest(bs)
    5
    >>> largest(BTree(1))
    1
    """
    assert t is not BTree.empty, 'BTree can not be BTree.empty'
    if t.right is BTree.empty:
        return t.label
    else:
        return largest(t.right)

    def second(t):
        """Return the second largest element of a binary search tree."""
        if t.is_leaf():
            return None
        elif t.right is BTree.empty:
            return largest(t.left)
        elif t.right.is_leaf():
            return t.label
        else:
            return second(t.right)


def contains(s, v):
    if s is BTree.empty:
        return False
    elif s.label == v:
        return True
    elif s.label < v:
        return contains(s.right, v)
    else:
        return contains(s.left, v)

def adjoin(s, v):
    if s is BTree.empty:
        return BTree(v)
    elif s.label == v:
        return s
    elif s.label < v:
        return BTree(s.label, s.left, adjoin(s.right, v))
    else:
        return BTree(s.label, adjoin(s.left, v), s.right)
    
        
