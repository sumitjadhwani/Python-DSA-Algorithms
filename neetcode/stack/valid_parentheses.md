# Valid Parentheses

https://neetcode.io/problems/validate-parentheses/question

## Question

You are given a string `s` consisting of the following characters: `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`.

The input string `s` is valid if and only if:

- Every open bracket is closed by the same type of close bracket.
- Open brackets are closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Return `true` if `s` is a valid string, and `false` otherwise.

### Example 1

```
Input: s = "[]"

Output: true
```

### Example 2

```
Input: s = "([{}])"

Output: true
```

### Example 3

```
Input: s = "[(])"

Output: false
```

Explanation: The brackets are not closed in the correct order.

### Constraints

- `1 <= s.length <= 1000`

## My Solution

### Solution 1

```python
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()

        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                temp = 'x'
                if len(stack)>0:
                    temp = stack.pop()

                if (c == '}' and temp!= '{'):
                    return False
                elif (c == ']' and temp!= '['):
                    return False
                elif (c == ')' and temp!= '('):
                    return False

        if(len(stack)>0): return False

        return True
```

### Solution 2

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map closing brackets to their matching opening brackets
        pairs = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in pairs: # If it's a closing bracket
                # If stack is empty, or the top of stack doesn't match, it's invalid
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop() # It's a match, remove it from the stack
            else: # If it's an opening bracket
                stack.append(c)

        # If stack is empty at the end, all brackets were matched
        return len(stack) == 0
```
