
'''
680. Valid Palindrome II - Easy
Given:
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
'''
'''
Solution:
1) the idea is almost identical to valid palindrome 1 problem, except one thing
2) in case when we reach that s[l] != s[r]:
3) we can skip either left or right char, so we need to try both with "or"
4) we get the subset without l or r, skipL, skipR
5) check weather they are equal themselves when reversed, reverse with operator [::-1]
'''

def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l+1:r+1], s[l:r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l += 1
            r -= 1
        return True
