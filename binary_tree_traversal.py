class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.value, end=' ')
        in_order_traversal(node.right)


def pre_order_traversal(node):
    if node:
        print(node.value, end=' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value, end=' ')


# Example tree creation
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Example usage
print("In-order Traversal:")
in_order_traversal(root)

print("\nPre-order Traversal:")
pre_order_traversal(root)

print("\nPost-order Traversal:")
post_order_traversal(root)
