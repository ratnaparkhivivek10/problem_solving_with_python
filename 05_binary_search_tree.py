class BinarySearchTree(object):
    def __init__(self, item):
        self.root = item
        self.left = None
        self.right = None

    def add(self, item):
        if item < self.root:
            if self.left is None:
                self.left = BinarySearchTree(item)
            else:
                self.left.add(item)
        else:
            if self.right is None:
                self.right = BinarySearchTree(item)
            else:
                self.right.add(item)

    def print_in_order(self):
        if self.left:
            self.left.print_in_order()
        print(self.root)
        if self.right:
            self.right.print_in_order()

bst = BinarySearchTree(5)
bst.add(8)
bst.add(7)
bst.add(1)
bst.add(3)
bst.add(9)
bst.add(2)

bst.print_in_order()
