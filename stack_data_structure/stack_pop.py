maxsize = 8
stack = [0] * maxsize
top = -1


def isempty():
    if top == -1:
        return 1
    else:
        return 0


def isfull():
    if top == maxsize:
        return 1
    else:
        return 0


def push(data):
    global top
    if isfull() != 1:
        top = top + 1
        stack[top] = data
    else:
        print("\n could not insert data, stack is full")

    return data

def peek():
    return stack[top]

def pop():
    global top
    data = 0
    if isempty() != 1:
        data = stack[top]
        top = top - 1
        return data
    else:
        print("could not retrieve data, stack is empty")

    return data


push(44)
push(10)
# push(62)
# push(123)
push(15)
print("Stack Elements: ")
for i in range(maxsize):
    print(stack[i], end=" ")
print("\nElements popped: ")
while isempty() != 1:
    data = pop()
    print(data, end=" ")

print("\n element at top of the stack: ", peek())