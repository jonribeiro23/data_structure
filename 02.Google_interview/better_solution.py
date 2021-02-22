array1 = ['a', 'b', 'c', 'z']
array2 = ['z', 'y', 'x']


def common_items(arr1: list, arr2: list) -> bool:
    # Convert the array into object
    dictionary = {}

    for item in arr1:
        dictionary[item] = True
    print(dictionary)

    for item in arr2:
        if item in dictionary:
            return True
    return False


def common_items_2(arr1: list, arr2: list) -> bool:
    # dict.fromkeys(<list>, <value to put in>)
    dictionary = dict.fromkeys(arr1, True)
    res = list(map(lambda x: x in dictionary, arr2))
    return res[0]


print(common_items_2(array1, array2))

