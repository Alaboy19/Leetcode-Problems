'''
203. Remove Linked List Elements
Given:
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
'''
'''
Solution:
1) create dummy node and copy to prev 
2) assign prev.next to head
3) iterate through current_node by while loop, remember next_node
4) if condition is set(node.val == val) -> prev.next = remembered next node
5) else prev = current
6) iterate by current = next_node
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current_node = head
        dummy = ListNode()
        prev_node = dummy
        prev_node.next = head  

        while current_node: 
            next_node = current_node.next
            if current_node.val == val:
                prev_node.next = next_node
            else:
                prev_node = current_node 
            current_node = next_node 

        return dummy.next
                
