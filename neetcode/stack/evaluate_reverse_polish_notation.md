# Evaluate Reverse Polish Notation

## Question

You are given an array of strings `tokens` that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

- The operands may be integers or the results of other operations.
- The operators include `'+'`, `'-'`, `'*'`, and `'/'`.
- Assume that division between integers always truncates toward zero.

### Example 1

```
Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5
```

Explanation: `((1 + 2) * 3) - 4 = 5`

### Constraints

- `1 <= tokens.length <= 10000`.
- `tokens[i]` is `"+"`, `"-"`, `"*"`, or `"/"`, or a string representing an integer in the range `[-200, 200]`.

## My Solution

### Solution 1

```python
import operator
from collections import deque

# 1. Define the mapping dictionary
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        if len(tokens) == 1:
            return int(tokens[0])
        result = 1
        for token in tokens:
            if token not in ('+', '-', '*', '/'):
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token in ops:
                    result = int(ops[token](a, b))
                stack.append(result)
        return result
```

### Solution 2

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t not in '+-*/':
                s.append(int(t))
            else:
                num2 = s.pop()
                num1 = s.pop()
                if t =='+':
                    s.append(num1+num2)
                elif t =='-':
                    s.append(num1-num2)
                elif t =='*':
                    s.append(num1*num2)
                else:
                    s.append(int(num1/num2))
        return s[-1]
```
