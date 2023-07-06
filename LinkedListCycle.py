'''
141. Linked List Cycle
Given:
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
'''
'''
Solution:
slow and fast pointer solution, fast runs twice fast and they meet at one point eventually because
1) firslty - fast will be behind in cylce at one point 
2) fast has 2 velocity 
3) slow has 1 velocity 
4) their difference is 1 velocity 
5) so, as the difference between nodes (by length) is integer, by ones 
6) they difference s eventually become zero since it is some integer value -= 1
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast:
            try:
                fast = fast.next.next
                slow = slow.next
            except:
                return False

            if fast == slow:
                return True 
