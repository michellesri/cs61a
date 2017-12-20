class Tree:
    def __init__(self, label, branches=[]):
        for c in branches:
            assert isinstance(c, Tree)
        self.label = label
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.label, branches_str)

    def is_leaf(self):
        return not self.branches

    def __eq__(self, other):
        return type(other) is type(self) and self.label == other.label \
               and self.branches == other.branches

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

    def copy_tree(self):
        return Tree(self.label, [b.copy_tree() for b in self.branches])


my_tree = Tree(5,
  [Tree(4,
        [Tree(1),
         Tree(2)]),
   Tree(6,
        [Tree(7,
              [])
              ]
              )
              ]
              )


def depth_first_search(t, target):
    print(t.label)
    if t.label == target:
        return True

    if t.is_leaf():
        return False

    boolean_list = [depth_first_search(t, target) for t in t.branches]

    for val in boolean_list:
        if val == True:
            return True
    return False

print(depth_first_search(my_tree, 1))

def depth_first_search_count(t, target):
    count = 0
    def inner():
        if t.label == target:
            return count
    return inner




print(depth_first_search_count(my_tree, 1))
