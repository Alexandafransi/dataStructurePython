from typing import Optional


class Node:
    def __init__(self, data: int, next: Optional['Node'] = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        p = self.head
        print("\n[", end="")
        while p:
            print(f" {p.data} ", end="")
            p = p.next
        print("]")

    def insert_at_begin(self, data: int):
        lk = Node(data)
        lk.next = self.head
        self.head = lk

    def delete_at_begin(self):
        self.head = self.head.next

    def deleteatend(self):
        linkedlist = self.head
        while linkedlist.next.next != None:
            linkedlist = linkedlist.next
        linkedlist.next = None

linked_list = LinkedList()
linked_list.insert_at_begin(12)
linked_list.insert_at_begin(13)
linked_list.insert_at_begin(14)
linked_list.insert_at_begin(15)
print("Linked list: ", end="")
linked_list.print_list()
linked_list.delete_at_begin()
print("Linked List after deletion: ", end="")
linked_list.print_list()
linked_list.deleteatend()
print("Linked List after deletion: ", end="")
linked_list.print_list()