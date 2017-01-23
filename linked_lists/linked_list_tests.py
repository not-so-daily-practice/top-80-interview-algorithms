from linked_lists.compare_linked_list_strings import compare_linked_list_strings
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

print("--------------------------------")

node_1a = LinkedListNode('g')
node_2a = LinkedListNode('e')
node_3a = LinkedListNode('e')
node_4a = LinkedListNode('k')
node_5a = LinkedListNode('s')
node_6a = LinkedListNode('a')

node_1a.next = node_2a
node_2a.next = node_3a
node_3a.next = node_4a
node_4a.next = node_5a
node_5a.next = node_6a

node_1b = LinkedListNode('g')
node_2b = LinkedListNode('e')
node_3b = LinkedListNode('e')
node_4b = LinkedListNode('k')
node_5b = LinkedListNode('s')
node_6b = LinkedListNode('b')

node_1b.next = node_2b
node_2b.next = node_3b
node_3b.next = node_4b
node_4b.next = node_5b
node_5b.next = node_6b

print(compare_linked_list_strings(node_1a, node_1b))

node_5b.next = None
print(compare_linked_list_strings(node_1a, node_1b))

node_5a.next = None
print(compare_linked_list_strings(node_1a, node_1b))
