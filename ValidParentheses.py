'''
Given:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example: 
Input: s = "()[]{}"
Output: true
Input: s = "(]"
Output: false
'''
def isValid(self, string: str) -> bool:
        close_open = {')':'(', '}':'{', ']':'['}
        open_stack = []
        closed_stack = []
        for char in string:
            if char not in close_open:
                open_stack.append(char)
            else:
                closed_stack.append(char)
                if not open_stack or close_open[closed_stack.pop()] != open_stack.pop():
                    return False
        return not open_stack and not closed_stack
