max = 6
intArray = [0] * max
front = 0
rear = -1
itemcount = 0


def isfull():
    return itemcount == max


def isempty():
    return itemcount == 0


def removedata():
    global front
    data = intArray[front + 1]
    if front == max:
        front = 0
    itemcount - 1
    return data


def insert(data):
    global rear, itemcount
    if not isfull():
        if rear == max - 1:
            rear = -1
        rear = rear + 1
        intArray[rear] = data
        itemcount + 1

insert(3)
insert(4)
insert(5)

print("Queue: ")
for i in range(max):
    print(intArray[i], end=" ")

while not isempty():
    n = removedata()
    print(n, end=" ")