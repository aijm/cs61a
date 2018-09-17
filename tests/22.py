from m21 import *
abcde = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.'}
flag = {'.': 0, '-': 1}

def morse(code):
    """Return a tree of morse code."""
    root = BTree(None)

    for letter, signals in sorted(code.items()):
        t = root
        for signal in signals:
            if t.branches[flag[signal]] is BTree.empty:
                t.branches[flag[signal]] = BTree(None)
            t = t.branches[flag[signal]]
        t.label = letter
    return root

def decode(signals, tree):
    t = tree
    for signal in signals:
        assert signal in flag, "Invalid signals."
        if t.branches[flag[signal]] is BTree.empty:
            return "Error: Invalid signals."
        t = t.branches[flag[signal]]
    return t.label

        




        


