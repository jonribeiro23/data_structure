# Find what pair of numbers are equals to sum
# [1, 2, 3, 9] Sum = 8
# [1, 2, 4, 4] Sum = 8

pairs_of_numbers1 = [1, 2, 3, 9]
pairs_of_numbers2 = [1, 2, 4, 4]

for number1 in pairs_of_numbers1:
    for number2 in pairs_of_numbers1:
        if number1 + number2 == 8:
            print(number1, ' + ', number2, ' = 8')

for number1 in pairs_of_numbers2:
    for number2 in pairs_of_numbers2:
        if number1 + number2 == 8:
            print(number1, ' + ', number2, ' = 8')

# Give 2 arrays, create a function that let's a user know (true/false) whether
# this two arrays contain any common item



def common_item(arr1: list, arr2: list) -> bool:
    for item_of_array1 in arr1:
        for item_of_array2 in arr2:
            if item_of_array1 == item_of_array2:
                return True
    return False


array1 = ['a', 'b', 'c', 'y']
array2 = ['z', 'y', 'x']

print(common_item({'a': 1}, array2))
