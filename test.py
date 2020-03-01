import sys
from queue import PriorityQueue
from collections import deque


class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"



class Node:
    def __init__(self, value, char=None):
        self.value = value
        self.left = None
        self.right = None
        self.char = char

    def get_value(self):
        return self.value

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    def has_char(self):
        return self.char != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.char}, {self.get_value()})"

    def __str__(self):
        return f"Node({self.char}, {self.get_value()})"


class Tree:
    def __init__(self, node):
        self.root = node

    def get_root_value(self):
        return self.root.value

    def join_tree(self, tree):
        value = self.get_root_value() + tree.get_root_value()
        new_node = Node(value)
        new_node.left = self.root
        new_node.right = tree.root
        self.root = new_node

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.root
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level
        return s

def huffman_encoding(data):
    # forest is a array of tree objects
    forest = []
    q = PriorityQueue()
    ch_set = set(data)
    for ch in ch_set:
        c = data.count(ch)
        n = Node(c, ch)
        t = Tree(n)
        forest.append(t)
        index = len(forest) - 1
        q.put((c, index))
    while q.qsize() > 1:
        a = q.get()
        b = q.get()
        tree1 = forest[a[1]]
        tree2 = forest[b[1]]
        tree1.join_tree(tree2)
        forest.append(tree1)
        index = len(forest) -1
        q.put((a[0]+b[0], index))

    tree = forest[q.get()[1]]

    dict = build_dictionary(tree)

    codedstr = []
    for char in data:
        codedstr.append(dict[char])
    return codedstr, tree

def build_dictionary(tree):
    s = ""
    dic = {}
    def traverse(node, code):
        if node:
            if node.has_char():
                print(f'{node.char}, {code}')
                dic[node.char] = code
            if node.has_left_child():
                traverse(node.get_left_child(), code + "1")
            if node.has_right_child():
                traverse(node.get_right_child(), code + "0")
    root = tree.root
    traverse(root, s)
    return dic

def build_reverse_dictionary(tree):
    s = ""
    dic = {}
    def traverse(node, code):
        if node:
            if node.has_char():
                print(f'{node.char}, {code}')
                dic[code] = node.char
            if node.has_left_child():
                traverse(node.get_left_child(), code + "1")
            if node.has_right_child():
                traverse(node.get_right_child(), code + "0")
    root = tree.root
    traverse(root, s)
    return dic

s = "sdjillaaa"
tree = huffman_encoding(s)
print(tree)
dic = build_dictionary(tree)

print(dic)