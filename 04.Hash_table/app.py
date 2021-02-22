test = {
    'name': 'John',
    'age': 29,
    'binary': lambda x, y: 2**x + y
}

print(test['binary'](5, 100))
del test['name']  # remove entry with key 'Name'
test.clear()      # remove all entries in dict
del test          # delete entire dictionary
