class Node:
    def __init__(self,data=None):
        self.next = None
        self.data = data


class SLLE:
    def __init__(self):
        self.head = None

    def listprint(self):
        val = self.head
        print("Linked List: ")
        while val is not None:
            print(val.data)
            val = val.next


l1 = SLLE()
l1.head = Node("23")
l2 = Node("44")
l3 = Node("45")
l4 = Node("46")
l5 = Node("47")

# linking the first Node to second node
l1.head.next = l2

l2.next = l3
l3.next = l4
l4.next = l5
l1.listprint()