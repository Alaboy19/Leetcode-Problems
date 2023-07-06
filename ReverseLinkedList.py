'''
Given:
206. Reverse Linked List - Easy
Given the head of a singly linked list, reverse the list, and return the reversed list.
Example:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''
'''
Solution:
1) next_node = prev_node = None 
2) start iterating while head:
3) assign next_node pointer to head.next, then 
4) head.next = prev_node
5) then before jumping to to the same with next node
6) assign prev_node as current node, - head
7) iterate finally by head = next_node
8) return the prev_node as (prev_last_node) and current first node  
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next_node = previous_node = None 
        while head:
            next_node = head.next
            head.next = previous_node
            previous_node = head
            head = next_node
        return previous_node
