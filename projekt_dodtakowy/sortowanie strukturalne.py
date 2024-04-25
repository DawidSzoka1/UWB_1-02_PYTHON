def sort_list(array: list):
    sorted_list = False
    right = len(array) - 1

    while not sorted_list:
        sorted_list = True
        for i in range(0, right):
            if array[i] > array[i + 1]:
                sorted_list = False
                array[i], array[i + 1] = array[i + 1], array[i]


test = [2, 1, 3, 4, 0, 10, 9]
sort_list(test)
print(test)


def find_in_sorted_list(array: list, find: int):
    left = 0
    right = len(array) - 1
    finded = False
    while not finded:
        finded = True
        mid = (left + right) // 2
        if array[mid] == find:
            return mid
        elif array[mid] < find:
            finded = False
            left = mid
            right += 1
        elif array[mid] > find:
            finded = False
            right = mid
            left -= 1
    return "Brak"


print(find_in_sorted_list(test, 0))
