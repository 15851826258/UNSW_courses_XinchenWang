import re


def myfind(s, char):
    pos = s.find(char)
    if pos == -1:  # not found
        return len(s) + 1
    else:
        return pos


def next_tok(s):  # returns tok, rest_s
    if s == '':
        return (None, None)
    # normal cases
    poss = [myfind(s, ' '), myfind(s, '['), myfind(s, ']')]
    min_pos = min(poss)
    if poss[0] == min_pos:  # separator is a space
        tok, rest_s = s[: min_pos], s[min_pos + 1:]  # skip the space
        if tok == '':  # more than 1 space
            return next_tok(rest_s)
        else:
            return (tok, rest_s)
    else:  # separator is a [ or ]
        tok, rest_s = s[: min_pos], s[min_pos:]
        if tok == '':  # the next char is [ or ]
            return (rest_s[:1], rest_s[1:])
        else:
            return (tok, rest_s)


def str_to_tokens(str_tree):
    # remove \n first
    str_tree = str_tree.replace('\n', '')
    out = []

    tok, s = next_tok(str_tree)
    while tok is not None:
        out.append(tok)
        tok, s = next_tok(s)
    return out


# Note: You need to pay attention to how to determine whether a node is a leaf node in this implementation.
class Tree(object):
    def __init__(self, name='ROOT', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.name

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)


def print_tree(root, indent=0):
    print(' ' * indent, root)
    if len(root.children) > 0:
        for child in root.children:
            print_tree(child, indent + 4)


# format: node, list-of-children
str_tree = '''
1  [2 [3 4       5          ]
   6 [7 8 [9]   10 [11 12] ]
   13
  ]
'''

str_tree = '''
1  
'''
toks = str_to_tokens(str_tree)
print(toks)


#
#
# t = Tree('*', [Tree('1'),
#                Tree('2'),
#                Tree('+', [Tree('3'),
#                           Tree('4')])])
# print_tree(t)


def make_tree(tokens):  # do not change the heading of the function
    for i in range(len(tokens)):
        if i == 0:  # The first must be the root
            tree = Tree(tokens[0])  # create a new tree
            former_ele = []
            parent = child = tree
            # former_ele.append(tokens[i])#append the first ele which is root
        elif tokens[i] == "[":
            former_ele.append(parent)
            parent = child  # the tree goes to another child
        elif tokens[i] == "]":
            parent = former_ele.pop(-1)  # Reduce the last one
        else:
            child = Tree(tokens[i])  # child is tree as well
            parent.add_child(child) #add parent to the child make it
    return tree


def max_depth(root):  # do not change the heading of the function
    max_list = []
    max_list.append(1)  # if there is no child the depth is 1
    if (root.children == None):  # the exit of recursion
        return 1  # the recursion goes to the bottom of tree
    for ele in root.children:
        max_list.append(max_depth(ele) + 1)  # recursive case
        #print(max_list)
    return max(max_list)  # In the whole list the max value is the depth


tt = make_tree(toks)
print_tree(tt)

print(max_depth(tt))
