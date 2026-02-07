# 20. Valid Parentheses
# Easy
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

def valid_parentheses(s: str):
    stack = []
    dict_symbols = {")": "(", "]": "[", "}": "{"}
    
    for char in s:
        if char in dict_symbols.values():  # Если это открывающая скобка
            stack.append(char)
        elif char in dict_symbols.keys():  # Если это закрывающая скобка
            if not stack or dict_symbols[char] != stack.pop():
                return False
    
    return not stack  # Стек должен быть пустым в конце


def main():
    print(valid_parentheses("()"))        # True
    print(valid_parentheses("([)]"))      # False
    print(valid_parentheses("()[]{}"))    # True
    print(valid_parentheses("(]"))        # False
    print(valid_parentheses("([])"))      # True
    print(valid_parentheses("("))         # False
    print(valid_parentheses("]"))         # False

main()