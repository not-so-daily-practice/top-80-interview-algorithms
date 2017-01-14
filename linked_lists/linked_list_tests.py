from linked_lists.linked_list import LinkedList
from linked_lists.linked_list_node import LinkedListNode

l_list = LinkedList()

node_5 = LinkedListNode(5)
node_10 = LinkedListNode(10)
node_7 = LinkedListNode(7)
node_3 = LinkedListNode(3)
node_1 = LinkedListNode(1)
node_9 = LinkedListNode(9)

l_list.sorted_node_insert(node_5)
l_list.sorted_node_insert(node_10)
l_list.sorted_node_insert(node_7)
l_list.sorted_node_insert(node_3)
l_list.sorted_node_insert(node_1)
l_list.sorted_node_insert(node_9)

l_list.print_list()

print("--------------------------------")

l_list.delete_node(l_list.head)

l_list.print_list()
