def linear_search(a,n,key):
    count = 0
    for i in range(n):
        if a[i] == key:
            print("The element is found at position ", (i+1))
            count +=1
    if count ==0:
        print("The element is not present in the array")


a = [14,44,55,663,3,56,66]
n = len(a)
key = 56
linear_search(a,n,key)
key = 444
linear_search(a,n,key)