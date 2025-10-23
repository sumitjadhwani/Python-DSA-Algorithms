'''
Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
'''

from collections import deque

def reverse_string(s: str) -> str:
    stack = deque()
    for c in s:
        stack.append(c)

    res = ""
    while stack:
        res+=stack.pop()

    return res
 
string = "We will conquere COVID-19"
reversed_string = reverse_string(string)

print(f'Original: "{string}"')
print(f'Reversed: "{reversed_string}"')



'''
Write a function in python that checks if paranthesis in the string are balanced or not. 
Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.

is_balanced("({a+b})")     --> True
is_balanced("))((a+b}{")   --> False
is_balanced("((a+b))")     --> True
is_balanced("))")          --> False
is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True

'''


from collections import deque

def is_balanced(s: str) -> bool:
    print(s)
    stack = deque()
    
    for c in s:
        if c in '{[(':
            stack.append(c)

        elif c == '}':
            if not stack:  # ✅ Check before popping
                return False
            res = stack.pop()
            if res != '{':
                return False
        
        elif c == ']':
            if not stack:  # ✅ Check before popping
                return False
            res = stack.pop()
            if res != '[':
                return False

        elif c == ')':
            if not stack:  # ✅ Check before popping
                return False
            res = stack.pop()
            if res != '(':
                return False
    
    return len(stack) == 0  # ✅ Check stack is empty


if __name__ == "__main__":
    print(is_balanced("({a+b})"))           # True
    print(is_balanced("))((a+b}{"))         # False
    print(is_balanced("((a+b))"))           # True
    print(is_balanced("))"))                # False
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))  # True
    print(is_balanced("({a+b})"))
    print(is_balanced(" "))


