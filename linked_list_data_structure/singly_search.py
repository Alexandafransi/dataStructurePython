class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        print("Linked List: ")
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def search(self, x):
        current = self.head
        count = 0

        while current is not None:
            if current.data == x:
                print("Element is found")
                count = count + 1
            current = current.next

        if count == 0:
            print("Element is not found in the list")


l1 = SLL()
l1.head = Node("444")
e2 = Node("55")
e3 = Node("33")
l1.head.next = e2
e2.next = e3
l1.listprint()
element = "33"
print("Element to be searched is : ", element)
l1.search(element)
