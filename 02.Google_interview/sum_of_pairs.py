# Find what pair of numbers are equals to sum
# [1, 2, 3, 9] Sum = 8
# [1, 2, 4, 4] Sum = 8

pairs_of_numbers1 = [1, 2, 3, 9]
pairs_of_numbers2 = [1, 2, 4, 4]


def has_pair_with_sum_8(arr: list) -> bool:
    return 8 in sum_pairs(arr)


def sum_pairs(arr: list):
    for i in range(len(arr)):
        try:
            if arr[i + 1]:
                summed_pairs = arr[i] + arr[i + 1]
                yield summed_pairs
        except IndexError:
            break


print(has_pair_with_sum_8(pairs_of_numbers1))
