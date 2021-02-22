strings = ['a', 'b', 'c', 'd']

# insert element in the array
# insert at the end
strings.append('e')  # O(1)

# insert at the specified position
strings.insert(0, 'f')  # O(n)
strings.insert(round(len(strings)/2), 'g')  # O(n/2)
print(strings)


# remove element
# removes the first matching value, not a specific index:
strings.remove('b')  # O(n)

# removes the item at a specific index and returns it.
strings.pop(3)  # O(1)

# removes the item at a specific index:
del strings[0]  # O(1)
print(strings)
