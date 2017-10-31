# Constructor
def tree(label, branches=[]):
    # for branch in branches:
        # assert is_tree(branch) # is the tree a tree???
    return [label] + list(branches)

# Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

# For convenience
def is_leaf(tree):
    return not branches(tree)


t = tree(1,
        [tree(3,
            [tree(4),
            tree(5),
            tree(6)]),
        tree(2)])

simple_tree = tree(3, [tree(4), tree(5)])

def tree_max(t):
    """Return the max of a tree (the largest number in a tree)."""
    return max([label(t)] + [branch for branch in branches(t)])

def square_tree(t):
    """Return a tree with the square of every element in t"""

    return tree(label(t) ** 2, [square_tree(branch) for branch in branches(t)])
