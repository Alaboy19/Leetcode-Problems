'''
83. Remove Duplicates from Sorted List
Given:
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
Input: head = [1,1,2,3,3]
Output: [1,2,3]
'''
'''
Solution:
0) handle the case when empty, if not head -> return head
1) assign previous to start and current to head.next
2) iterate current and if curr.val == prev.val, prev.next -> curent.next, prev stays 
3) if not, prev = curent 
4) iterate curr = curr.next 
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
             
        prev = head 
        current = head.next

        while current:
            if current.val == prev.val:
                prev.next = current.next
            else:
                prev = current
            current = current.next 

        return head
