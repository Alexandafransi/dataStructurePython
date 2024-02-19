maxsize = 8
stack = [0] * maxsize
top = -1


def isfull():
    if top == maxsize:
        return 1
    else:
        return 0


def push(data):
    global top
    print("this is top ", top)
    if isfull() != 1:
        top = top + 1
        stack[top] = data

    else:
        print("Could not insert data, Stack is full.")
    return data


push(22)
push(23)
push(24)
push(25)
push(26)
push(27)
push(27)
push(27)
push(27)
print("Stack Elements: ")
for i in range(maxsize):
    print(f"{stack[i]}\n")
