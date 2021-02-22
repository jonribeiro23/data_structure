# merge sorted array
array_1 = [0, 3, 4, 31]
array_2 = [4, 6, 30]


def valid_array(arr1, arr2):
    return (arr1 is not None and arr2 is not None) and (arr1 != [] and arr2 != [])


def merge_sorted_array(arr1: list, arr2: list) -> list:
    new_array = build_array(arr1, arr2)
    sorted_array = []
    while new_array:
        less_number = less(new_array)
        sorted_array.append(less_number)
        new_array.remove(less_number)
    return remove_repeated(sorted_array)


def less(arr: list) -> int:
    less_number = arr[0]
    for item in arr:
        if less_number > item:
            less_number = item
    return less_number


def build_array(arr1: list, arr2: list) -> list:
    for item in arr2:
        arr1.append(item)
    return arr1


def remove_repeated(arr: list) -> list:
    for i in range(len(arr) - 1):
        try:
            if arr[i] == arr[i + 1]:
                arr.pop(i)
        except IndexError:
            break
    return arr


# ========================================================

def merge_sorted_array_2(arr1: list, arr2: list) -> list:
    if valid_array(arr1, arr2):
        new_array = arr1 + arr2
        array_merged = []
        while new_array:
            less_number = less(new_array)
            array_merged.append(less_number)
            new_array.remove(less_number)
        return array_merged
    return 'Invalid array'


print(merge_sorted_array_2(array_1, []))
# print(array_1.pop())
