class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        p = self.head
        print("\n[", end="")
        while p is not None:
            print(" ", p.data, " ", end="")
            p = p.next
        print("]")

    def insertatbegin(self, data):
        lk = Node(data)
        lk.next = self.head
        self.head = lk

    def deletenode(self, key):
        temp = self.head
        if temp is not None and temp.data is key:
            self.head = temp.next
            return

        while temp is not None and temp.data is not key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next


llist = LinkedList()
llist.insertatbegin(12)
llist.insertatbegin(22)
llist.insertatbegin(30)
llist.insertatbegin(40)
llist.insertatbegin(55)
print("Original Linked List: ", end="")
# print list
llist.printList()
llist.deletenode(30)
print("Linked List after deletion: ", end="")
# print list
llist.printList()
