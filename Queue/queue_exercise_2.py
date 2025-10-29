from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.append(val)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.buffer.popleft()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)
        
    def print_queue(self):
        """
        Prints the current contents of the queue.
        """
        print(f'Current queue: {list(self.buffer)}')


def generate_binary_numbers(n):
    """
    Generates and prints binary numbers from 1 to n using a Queue.
    """
    if n <= 0:
        return

    queue = Queue()
    queue.enqueue("1")

    # Repeat n times to generate n binary numbers
    for i in range(1, n + 1):
        # Dequeue the next binary number
        binary_number = queue.dequeue()
        print(f"[{i}] Dequeued: {binary_number}")

        # Enqueue the next two binary numbers by appending "0" and "1"
        queue.enqueue(binary_number + "0")
        queue.enqueue(binary_number + "1")
        
        # Print the queue's state after each iteration
        queue.print_queue()
        print("-" * 20)

# Call the function to print binary numbers from 1 to 10
generate_binary_numbers(10)
