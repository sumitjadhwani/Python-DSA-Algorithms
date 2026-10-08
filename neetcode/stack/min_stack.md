# Min Stack

## Question

Design a stack class that supports the `push`, `pop`, `top`, and `getMin` operations.

- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

Each function should run in `O(1)` time.

### Example 1

```
Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]
```

Explanation:
```
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1
```

### Constraints

- `-2^31 <= val <= 2^31 - 1`.
- `pop`, `top` and `getMin` will always be called on non-empty stacks.
- At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.

## My Solution

```python
from collections import deque

class MinStack:

    def __init__(self):
        # We store tuples of (value, minimum_at_this_point)
        self.stack = deque()

    def push(self, val: int) -> None:
        # If stack is empty, the current val is the minimum.
        # Otherwise, compare val with the minimum of the previous top element.
        if not self.stack:
            current_min = val
        else:
            current_min = min(val, self.stack[-1][1])

        self.stack.append((val, current_min))

    def pop(self) -> None:
        # Removes the top tuple from the right side
        self.stack.pop()

    def top(self) -> int:
        # Accesses the value of the top tuple (index -1, first element)
        return self.stack[-1][0]

    def getMin(self) -> int:
        # Accesses the minimum of the top tuple (index -1, second element)
        return self.stack[-1][1]
```
