'''
234. Palindrome Linked List
Given:
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

Input: head = [1,2,2,1]
Output: true
'''
'''
Solution:
the key thing to not use O(n) extra space is to modify the given linked list in place
1) iterate slow and fast pointer to get to exact half of the llist 
2) break the list to two n/2 llist
3) reverse the second llist
4) iterate and compare each - > false if not equal  
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from copy import deepcopy
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True 

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head_second = slow.next
        slow.next = None
        
        head_sorted_second = self.reverseList(head_second)
        head_first = head
        
        while head_first and head_sorted_second:
            if head_first.val != head_sorted_second.val:
                return False
            head_first = head_first.next
            head_sorted_second = head_sorted_second.next 

        return True 

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next_node = previous_node = None
        while head:
            next_node = head.next
            head.next = previous_node
            previous_node = head
            head = next_node
        return previous_node
