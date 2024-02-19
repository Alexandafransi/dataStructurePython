max = 6
intarray = [0]*max
front=0
rear = -1
itemcount = 0

def isfull():
    return itemcount == max

def isempty():
    return itemcount == 0

def insert(data):
    global rear,itemcount
    if not isfull():
        if rear == max-1:
            rear=-1
        rear +=1
        intarray[rear] = data
        itemcount +=1

def peek():
    return intarray[front]

def removedata():
    global front,itemcount
    data = intarray[front]
    if front == max-1:
        front = 0
    else:
        front +=1
    itemcount -=1
    return data


insert(3)
insert(33)
insert(30)
insert(35)
insert(36)
insert(40)

print("Queue: ")
for i in range(max):
    print(intarray[i], end=" ")
num = removedata()
print("\nElement removed: ",num)
print("Update Queue: ")
# while not isempty():
#     n = removedata()
#     print(n,end=" ")

print("\n Element at front: ", peek())