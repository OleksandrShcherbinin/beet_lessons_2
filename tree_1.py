class BinaryTreeNode:
    def __init__(self, value: int | float):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.value)


class BinaryTreeSearch:

    def __init__(self, root: BinaryTreeNode):
        self.root = root

    def add(self, value, node=None):
        if not node:
            node = self.root

        if value < node.value:
            if not node.left:
                node.left = BinaryTreeNode(value)
            else:
                self.add(value, node.left)
        else:
            if not node.right:
                node.right = BinaryTreeNode(value)
            else:
                self.add(value, node.right)

    def search(self, value):
        node = self.root

        while node:
            print(node.value)
            if node.value == value:
                return True
            if node.value > value:
                node = node.left
            else:
                node = node.right

        return False

    def visit(self, node):
        print(node.value, end='->')

    def preorder(self, node):
        if not node:
            return
        self.visit(node)
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        if not node:
            return

        self.inorder(node.left)
        self.visit(node)
        self.inorder(node.right)

    def postorder(self, node):
        if not node:
            return

        self.postorder(node.left)
        self.postorder(node.right)
        self.visit(node)


root_node = BinaryTreeNode(7)
search_tree = BinaryTreeSearch(root_node)

search_tree.add(4)
search_tree.add(6)
search_tree.add(5)
search_tree.add(2)
search_tree.add(1)
search_tree.add(3)
search_tree.add(11)
search_tree.add(13)
search_tree.add(14)
search_tree.add(12)
search_tree.add(9)
search_tree.add(8)
search_tree.add(7)

search_tree.search(5)

# search_tree.preorder(root_node)
# search_tree.inorder(root_node)
# search_tree.postorder(root_node)


class Expression:
    pass


class Multiplication(Expression):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return '(' + str(self.left) + '*' + str(self.right) + ')'

    def eval(self, variables):
        return self.left.eval(variables) * self.right.eval(variables)


class Plus(Expression):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return '(' + str(self.left) + '+' + str(self.right) + ')'

    def eval(self, variables):
        return self.left.eval(variables) + self.right.eval(variables)


class Constant(Expression):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def eval(self, variables):
        return self.value


class Variable(Expression):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def eval(self, variables):
        return variables[self.name]


variables = {
    'x': 2,
    'y': 4
}

expression_1 = Multiplication(Constant(3), Plus(Variable('y'), Variable('x')))

expression_2 = Plus(Variable('x'), Multiplication(Constant(3), Variable('y')))

print(expression_1)

print(expression_2)

print(expression_1.eval(variables))

print(expression_2.eval(variables))
