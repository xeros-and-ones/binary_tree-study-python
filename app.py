from binary_tree import BinaryTree
from node import Node

tree = BinaryTree(Node(9))
tree.add(Node(4))
tree.add(Node(20))
tree.add(Node(2))
tree.add(Node(29))
tree.add(Node(15))
tree.add(Node(30))
tree.add(Node(6))


# print("-----------------------")
# tree.postorder()

tree.inorder()
print("-----------------------")
tree.preorder()
tree.delete(20)
print("-----------------------")
tree.preorder()

print(tree)
