'''
9. Palindrome Number
Given:
Given an integer x, return true if x is a palindrome, and false otherwise.
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Solution:
0) the idea is to get each digit from less significant and append it to list
1) then check the list with two pointer for polindromness 
2) in order to get less significant digit by one by one, do while loop and append x % 10, then x = x//10, while x:
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        lst = []
        while x:
            right_digit = x % 10
            lst.append(right_digit)
            x = x // 10 

        l, r = 0, len(lst) - 1
        while l < r:
            if lst[l] != lst[r]:
                return False
            l += 1
            r -= 1
        
        return True 
