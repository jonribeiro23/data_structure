# Create a function that reverses a string
# "Hi My name is Jon" should be
# "noJ si eman yM iH"

def reverse_string(string: str) -> str:
    try:
        if string is None or string == '' or len(string) < 2:
            return 'Invalid string.'

        inverted_string = ''
        for letter in range(len(string) - 1, -1, -1):
            inverted_string += string[letter]

    except TypeError:
        return 'String not found'
    else:
        return inverted_string


def reverse_string_2(string: str) -> str:
    if string is None or string == '' or len(string) < 2:
        return 'Invalid string.'

    return ''.join(list(reversed(string)))


reverse_string_3 = lambda string: ''.join(list(reversed(string)))

print(reverse_string('String not found'))
print(reverse_string_2('String not found'))
print(reverse_string_3('String not found'))
