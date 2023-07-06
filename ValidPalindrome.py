'''
125. Valid Palindrome - Easy - Two Pointers
Given:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise
'''
def isPalindrome(self, s: str) -> bool:
        string = [char.lower() for char in s if char.isalnum()]
        f_pt, s_pt = 0, len(string) - 1
        while f_pt < s_pt:
            if string[f_pt] != string[s_pt]:
                return False
            f_pt += 1
            s_pt -= 1

        return True
'''
Solution:

'''
