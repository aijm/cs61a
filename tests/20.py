class Link:
    """Linked List"""
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __len__(self):
        num, L = 0, self
        while L is not Link.empty:
            num += 1
            L = L.rest
        return num

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(self.first)
        else:
            return 'Link({}, {})'.format(self.first, repr(self.rest))
    
    def __str__(self):
        output = ''
        head = self
        while head is not Link.empty:
            output = output + ' ' + str(head.first)
            head = head.rest
        output = output.strip()
        return output

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value



def filter_link(f, s):
    """Return elements e of s for which f(e) is true."""
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered

def extend_link(s, t):
    if s is Link.empty:
        return t
    else:
        head = s
        while head.rest is not Link.empty:
            head = head.rest
        head.rest = t
        return s


# Sets as unsorted sequences

def empty(s):
    return s is Link.empty

def contains(s, v):
    """Return true if set s contains value v as an element.
    
    >>> s = Link(1, Link(3, Link(2)))
    >>> contains(s, 2)
    True
    >>> contains(s, 4)
    False
    """
    head = s
    while not empty(head):
        if head.first == v:
            return True
        head = head.rest
    return False

def adjoin(s, v):
    """Return Set s adjoin v"""
    if contains(s, v):
        return s
    else:
        return Link(v, s)

def intersect(set1, set2):
    in_set2 = lambda v: contains(set2, v)
    return filter_link(in_set2, set1)

def union(set1, set2):
    not_in_set2 = lambda v: not contains(set2, v)
    set1_not_set2 = filter_link(not_in_set2, set1)
    return extend_link(set1_not_set2, set2)


def add(s, v):
    """Add v to a ordered set s and return s.

    >>> s = Link(1, Link(3, Link(5)))
    >>> add(s, 0)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 4)
    Link(0, Link(1, Link(3, Link(4, Link(5)))))
    >>> add(s, 6)
    Link(0, Link(1, Link(3, Link(4, Link(5, Link(6))))))
    >>> t = Link(1)
    >>> add(t, 0)
    Link(0, Link(1))
    """
    
    if empty(s):
        return Link(v)
    head = s
    if head.first > v:
        # s = Link(v, s) #error: assigment, then s will rebind to a new object
        # s.first, s.rest = v, s # error s.rest = s
        s.first, s.rest = v, Link(s.first, s.rest)
        return s
    # head.first <= v
    while not empty(head.rest) and head.rest.first <= v:
        head = head.rest
    if head.first == v:
        return s
    else:
        head.rest = Link(v, head.rest)
        return s

    


    