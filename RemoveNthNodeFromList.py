'''
19. Remove Nth Node From End of List
Given:
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
'''
'''
Solution:
1) create dummy tail node and tail.next = head 
2) l_ptr = r_ptr = tail
3) find r_ptr, (r_ptr = l_ptr + n), so iterate n time and assign node to r_ptr
4) if r_ptr reaches the end (if not right_pointer.next -> left_ptr.next = left_ptr.next.next, left_ptr.next.next is guaranteed since at least one space between l_ptr and r_ptr) 
5) if 4 happens, break, else l_ptr, r_ptr += 1
6) return tail.next 
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = ListNode() 
        tail.next = head
        left_pointer = right_pointer = tail

        while n > 0:
            right_pointer = right_pointer.next
            n -= 1

        while left_pointer and right_pointer:
            if not right_pointer.next:
                left_pointer.next = left_pointer.next.next
                break
            left_pointer = left_pointer.next
            right_pointer = right_pointer.next

        return tail.next
