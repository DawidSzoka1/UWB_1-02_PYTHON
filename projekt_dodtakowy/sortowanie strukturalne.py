def sort_list(array: list):
    sorted_list = False
    right = len(array)-1

    while not sorted_list:
        sorted_list = True
        for i in range(0, right):
            if array[i] > array[i+1]:
                sorted_list = False
                array[i], array[i+1] = array[i+1], array[i]


test = [2, 1, 3, 4, 0, 10, 9]
sort_list(test)
print(test)
