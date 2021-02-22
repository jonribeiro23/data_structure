from stack import Stack2

stack = Stack2()
stack.push('dog')
stack.push('cat')
stack.push('horse')
stack.push('bird')
r = stack.peek()
print(r.value)
stack.pop()
r = stack.peek()
print(r.value)

