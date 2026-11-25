my_queue: list[str] = []

def enqueue(item: any) -> None:
    """Adds the item to the end of the queue"""
    my_queue.append(item)
    
def is_empty() -> bool:
    """Checks if the queue is empty"""
    return len(my_queue) == 0
    
def dequeue() -> any:
    """Removes and returns the first customer"""
    if not is_empty():
        return my_queue.pop(0)
    return "Queue is empty"

def peek() -> any:
    """Returns the first item of the queue"""
    return my_queue[0]

def size() -> int:
    """Gets the size of the queue"""
    return len(my_queue)


enqueue("Alice")
enqueue("Bob")
enqueue("Charlie")
enqueue("Diana")

print("Peeked:", peek())

print("Dequeued:", dequeue())
print("Dequeued:", dequeue())
print("Dequeued:", dequeue())
print("Dequeued:", dequeue())
print("Dequeued:", dequeue())