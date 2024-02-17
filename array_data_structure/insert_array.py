# # this program is for array insertion
#
#
#
# def insert(arr, element):
#     arr.append(element)
#
#
# number_arry = [0,0,0]
#
# print("array before insertion: ")
# for x in range(len(number_arry)):
#     print("",[x], " = ", number_arry[x])
#
#
# print("Inserting elements...")
# for x in range(len(number_arry)):
#     print("this is array ", number_arry)
#     # number_arry.append(x)
#     # number_arry[x] = x+1
#     insert(number_arry,x+1)
#
# print("value ", number_arry)
# print("Array after insertion: ")
# for x in range(len(number_arry)):
#     print([x], " = ", number_arry[x])

def insert_array(arry, element):
    arry.append(element)


arry = []
for y in range(3):
    x = input(f"enter array value {y+1}: ")
    insert_array(arry, x)

print(len(arry))

# insert into specific index
arry[0] = '100'
print("this is array elements ",arry)

# insert into last element
last_index = len(arry)-1
a = input("enter array value you want to insert last ")
arry[last_index] = a
print("new array ", arry)