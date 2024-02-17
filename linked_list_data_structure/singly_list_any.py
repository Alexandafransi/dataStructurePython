class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None


class SLLA:
    def __init__(self):
        self.head = None


    def listprint(self):
        val = self.head
        while val is not None:
            print(val.data)
            val = val.next

    def insert_at_pos(self,nodeatpos,newdata):
        if nodeatpos is None:
            print("the mentioned node is absent")
            return
        newNode = Node(newdata)
        newNode.next = nodeatpos.next
        nodeatpos.next = newNode


l1 = SLLA()
# number_of_node = input("how many number of node do u want to add? \n")
# for i in range(int(number_of_node)):
#     input_node = input(f"enter node {i+1}")
#     if l1.head == None:
#         l1.head = Node(input_node)
#     Node(input_node)

l1.head = Node("233")
l2 = Node("444")
l3 = Node("445")
l4 = Node("446")
l1.head.next = l2
l2.next = l3
l3.next = l4

l1.insert_at_pos(l1.head.next,"122")
l1.listprint()

# a = input("where do u want to add another node? ")