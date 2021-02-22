arr = [1, 2, 3, 4, 5]


def log_all_pairs(arg):
    return list(map(lambda x: 2**x, arg))


def print_all_pairs(arg):
    for i in range(len(arg)):
        for j in range(len(arg)):
            print(f'{arg[i]}{arg[j]} ', end='')
        print()


# print(log_all_pairs(arr))
print_all_pairs(arr)
