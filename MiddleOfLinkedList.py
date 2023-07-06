'''
876. Middle of the Linked List
Given:
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
'''
'''
Solution:
1) slow = fast = head
2) while fast and fast.next: iterate slow by one, fast by two 
3) return where slow stops 

the thing is that it returns middle when fast.next is None and middle + 1 if fast is None by the rules,
so they(both slow and fast) must start at head 

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow 
