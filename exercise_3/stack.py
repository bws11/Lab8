my_stack: list[str] = []

def push(item: any) -> None:
    """Adds the item to the top of the stack"""
    my_stack.append(item)
    
def is_empty() -> bool:
    """Checks if the stack is empty"""
    return len(my_stack) == 0
    
def pop() -> any:
    """Removes and returns the top item"""
    if not is_empty():
        return my_stack.pop()
    return "Stack is empty"

def peek() -> any:
    """Returns the top items without removing it"""
    return my_stack[-1]

def size() -> int:
    """Gets the size of the stack"""
    return len(my_stack)


for i in range(4):
    user_word = str(input("Please enter a word: "))
    push(user_word)
    
print("Current document: ", ' '.join(my_stack))

print("Undoing the last two words...")
pop()
pop()

print("Updated document: ", ' '.join(my_stack))
