'''
160. ReorderList
Given:
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
Input: head = [1,2,3,4]
Output: [1,4,2,3]
'''
'''
Solution:
1) use slow pointer and fast pointer to find the end of the first half and start of the second half (point end of first to None)
2) then reverse the second half by using previous question function reverse linked list question
3) then just zig zag point first to i th of second, ith of second to i + 1 of first llist
4) use temp_top and temp_bottom to save next nodes and iterate head_top and head_bottom further
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


    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head_second = slow.next
        slow.next = None
        
        head_bottom = self.reverseList(head_second)
        head_top = head

        while head_top and head_bottom:
            temp_top = head_top.next
            temp_bot = head_bottom.next

            head_top.next = head_bottom
            head_bottom.next = temp_top

            head_top = temp_top
            head_bottom = temp_bot

        return head
