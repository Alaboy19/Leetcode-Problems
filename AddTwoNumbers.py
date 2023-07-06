'''
 Add Two Numbers
Given:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''
'''
Solution:
the key things here is to 
1) create dummy and assign to prev_node
2) while l1 and l2 is not None: iterate and compute sum, if sum >=10, assign new_complement
3) create new node and prev.next = new_node
4) at the end assign prev = new_node
5) iterate l1 and l2 if exist, assign to just None 
6) handle the edge case when there is no more list and complement stays 1 
7) in 6 case - create new node of val = 1 and point to it before the end of execution
8) return the dummy.next 
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        previous_node = dummy
        complement = new_complement = summa = val1 = val2 = 0  
        while l1 or l2:     
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 
            summa = val1 + val2 + complement
        
            if summa >= 10:
                summa = summa % 10 
                new_complement = 1
            else: 
                new_complement = 0 

            new_node = ListNode(summa, None)
            previous_node.next = new_node

            previous_node = new_node
            complement = new_complement
            l1 = None if not l1 else l1.next
            l2 = None if not l2 else l2.next

            if not l1 and not l2 and complement != 0:
                previous_node.next = ListNode(1, None)
            
        return dummy.next
