from trees.check_if_preorder_traversal import check_if_preorder_traversal
from trees.maximum_sum_path import max_sum_path_tree
from trees.minimum_depth import min_depth
from trees.node import Node

print("--------------------------------\n")
print("Find min Depth of Binary Tree")
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

root = Node(10)
node_a = Node(2)
node_b = Node(10)
node_c = Node(20)
node_d = Node(1)
node_e = Node(-25)
node_f = Node(3)
node_g = Node(4)

root.left = node_a
root.right = node_b
node_a.left = node_c
node_a.right = node_d
node_e.left = node_e
node_e.left = node_f
node_e.right = node_g

print("--------------------------------\n")
print("Find Path in Tree that has Largest Possible Sum")
print(max_sum_path_tree(root))

print("--------------------------------\n")
print("Check if Array is a Preorder Traversal of a Binary Tree")
arr = [2, 4, 3]
print(check_if_preorder_traversal(arr))

arr = [2, 4, 1]
print(check_if_preorder_traversal(arr))

arr = [40, 30, 35, 80, 100]
print(check_if_preorder_traversal(arr))

arr = [40, 30, 35, 20, 80, 100]
print(check_if_preorder_traversal(arr))
