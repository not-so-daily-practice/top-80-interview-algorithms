from linked_lists.linked_list_node import LinkedListNode


class LinkedList(object):
    """
    Singly Linked List
    """

    def __init__(self):
        self.head = None

    def push(self, data):
        """
        Add a node to the front of the list
        :param data: data to add
        """
        new_head = LinkedListNode(data)
        new_head.next = self.head
        self.head = new_head

    def print_list(self):
        """
        Utility to iterate over list and print each node
        """
        head = self.head
        while head:
            print(head.data)
            head = head.next

    def sorted_node_insert(self, node):
        """
        Insert a node in its sorted position
        :param node: node to insert
        """
        if self.head is None:
            node.next = self.head
            self.head = node
        elif self.head.data >= node.data:
            node.next = self.head
            self.head = node
        else:
            curr = self.head
            while curr.next and curr.next.data < node.data:
                curr = curr.next

            node.next = curr.next
            curr.next = node

    def delete_node(self, node):
        """
        Given a linked list node, find and remove it
        :param node: node to delete
        """
        if self.head == node:
            if self.head.next is None:
                raise Exception("Cannot have empty list")

            # copy next node data to head
            self.head.data = self.head.next.data

            # store next node link
            node = self.head.next

            # remove next node link
            self.head.next = node.next.next

        else:
            prev = self.head
            # get node before node to be deleted
            while prev.next is not None and prev.next is not node:
                prev = prev.next

            # check that node is in list
            if prev.next is None:
                raise Exception("Node to be deleted does not exist")

            prev.next = prev.next.next
