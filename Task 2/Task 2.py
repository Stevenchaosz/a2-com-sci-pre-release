class Node:
    def __init__(self, color):
        self.color = color
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def store_binary_tree(self):  # task 2.3
        self.root = Node("maroon")
        self.root.left = Node("black")
        self.root.right = Node("silver")
        self.root.left.left = Node("amber")
        self.root.left.right = Node("indigo")
        self.root.right.left = Node("grey")
        self.root.right.right = Node("red"),
        self.root.left.right.left = Node("violet")
        self.root.left.right.right = Node("lime green")

    # task 2.4
    def add_base(self, color):
        if self.root is None:
            self.root = Node(color)
        else:
            self.add_general(color, self.root)

    def add_general(self, color, node):
        if color < node.color:
            if self.root is not None:
                self.add_general(color, node.left)
            else:
                node.left(color)
        else:
            if node.right is not None:
                self.add_general(color, node.right)
            else:
                node.right = Node(color)

    # task 2.5
    def find_node(self, color):
        if self.root is not None:
            return self.find_general(color, self.root)
        else:
            return None

    def find_general(self, color, node):
        if color == node.color:
            return node
        elif color < node.color and (node.left is not None):
            return self.find_general(color, node.left)
        elif color > node.color and (node.right is not None):
            return self.find_general(color, node.right)

    # task 2.6
    def out_tree_from_node(self, root):
        arr = []
        if root is not None:
            arr.append(self.out_tree_from_node(root.left))
            arr.append(root.color)
            arr.append(self.out_tree_from_node(root.right))
        return arr

    def out_tree(self):
        return self.out_tree_from_node(self.root)
