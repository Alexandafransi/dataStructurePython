class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        print("linked list: ")
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def addAtBeginning(self, newdata):
        newNode = Node(newdata)
        # update the new nodes next val to existing node
        newNode.next = self.head
        self.head = newNode


l1 = SLL()
l1.head = Node("777")
e2 = Node("300")
e3 = Node("33")
l1.head.next = e2
e2.next = e3

l1.addAtBeginning("122")
l1.listprint()