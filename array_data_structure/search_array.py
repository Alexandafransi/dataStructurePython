def append_item(arry,element):
    arry.append(element)

def search_array(arr,element):
    for x in range(len(arr)):
        if arr[x] == element:
            return "it exist"


array_element = []
a = input("enter length of your array list \n")
print("start enter your value")
for x in range(int(a)):
    y = input(f"{x+1} value \n")
    append_item(array_element,y)

print("your array values = ",array_element)

n = input("please enter number you want to search in your list \n")
result = search_array(array_element,n)
if result == "it exist":
    print("your number ",n ," exist in array list")
else:
    print("your number ",n ," does not exist in array list")
