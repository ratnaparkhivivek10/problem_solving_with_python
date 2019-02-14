class BinarySearchTree(object):
    def __init__(self, item):
        self.root = item
        self.left = None
        self.right = None

    def add(self, item):
        if item <= self.root:
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
        pass