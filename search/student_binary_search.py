def student_search(student_names, low, high, target_name):
    # low, high = 0, len(student_names) - 1

    mid = (low + high) // 2
    if low <= high:
        if student_names[mid] == target_name:
            print("The element is present at index: ", mid, " and the name is: ", student_names[mid])

        elif target_name < student_names[mid]:
            student_search(student_names, low, mid - 1, target_name)

        elif student_names[mid] < target_name:
            student_search(student_names, mid + 1, high, target_name)

    if low > high:
        print("Unsuccessful Search: ", target_name)


student_names = ["Yvonne", "Bob", "Frank", "David", "Eline", "Alex", "Grace"]
n = len(student_names)
low = 0
high = n - 1
target_student = "Frank"
print("This is sorted student names: ",sorted(student_names))
student_search(sorted(student_names), low, high, target_student)
target_student = "Maganga"
student_search(sorted(student_names), low, high, target_student)
