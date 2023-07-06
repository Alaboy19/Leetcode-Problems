'''
155. Min Stack - Medium 
Given: 
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
'''

class MinStack:
    def __init__(self):
        self.items = []
        self.min_element = []

    def push(self, val: int) -> None:
        if len(self.min_element) == 0:
            self.min_element.append(val)
        else:
            if val <= self.min_element[-1]:
                self.min_element.append(val)
        self.items.append(val)

    def pop(self) -> None:
        if len(self.min_element) > 0 and self.min_element[-1] == self.items[-1]:
            self.min_element.pop()
        return self.items.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        if len(self.min_element) > 0:
            return self.min_element[-1]
        return None
