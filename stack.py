# the first idea: use the default 'list' function to realize stack

stack = []

# push operation is the original append function
def push(data):
    stack.append(data)
    return stack

def size(stack):
    return len(stack)

print(push(4))
print(size(stack))
stack.append(3)
print(stack)

# pop function is the original pop function

print(stack.pop())


