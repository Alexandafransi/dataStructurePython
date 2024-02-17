def delete_array(arry, element):
    arry.remove(element)

def delete_all(arry):
    arry.clear()

arry_element = [22, 33, 44, 55, 6, 6]
print(arry_element)
delete_array(arry_element, arry_element[1])
delete_all(arry_element)
print(arry_element)
