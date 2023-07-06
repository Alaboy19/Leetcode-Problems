'''
148. Sort List - Medium
Given:
Given the head of a linked list, return the list after sorting it in ascending order.
Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
'''
'''
Solution:
0) create an array where i will store (val, ptrToNode)
1) iterate through the linlist and append to array
2) create a dummy node pointing to null 
3) get prev variable and prev = dummy 
4) iterate thorugh list and make prev.next = node, prev = node
5) when done, make last node pointing to none and return dummy.next  
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mylist = []
        
        curr = head 
        while curr:
            # do staff 
            val, ptr = curr.val, curr
            mylist.append((val, ptr))
            curr = curr.next 

        mylist = sorted(mylist, key= lambda x: x[0])

        dummy = ListNode(0, None)
        prev = dummy

        for _, node in mylist:
            prev.next = node
            prev = node

        prev.next = None  

        return dummy.next 
