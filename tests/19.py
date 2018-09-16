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
    
    
class Tree:
    empty = []
    def __init__(self, label, branches=empty):
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
        

        
