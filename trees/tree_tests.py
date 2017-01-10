from trees.minimum_depth import min_depth
from trees.node import Node

root = Node(2)
node2 = Node(2)
node4 = Node(4)
node5 = Node(5)
node5b = Node(5)
node6 = Node(6)
node7 = Node(7)
node9 = Node(9)
node11 = Node(11)

root.left = node7
root.right = node5
node7.left = node2
node7.right = node6
node6.left = node5b
node6.right = node11
node5.right = node9
node9.left = node4

print(min_depth(root))
