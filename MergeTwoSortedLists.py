'''
21. Merge Two Sorted Lists
Given:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''
'''
Solution:
1) create dummy node and point to None 
2) create new pointer of dummy node itself as tail, tail = dummy 
3) while list1 and list2, iterate
4) compare list1.val and list2.val and assign tail.next to lesser one, lesser iterate by lesser = lesser.next
5) then, check if one of them(list1 and list2) left, not ended
6) append to tail.next the left one, only one of them will be left
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy 

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
