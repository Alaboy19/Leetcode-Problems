'''
217. Contains Duplicate - Easy
Given: 
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False 

        for c in set(s):
            if t.count(c) != s.count(c):
                return False 

        return True 
'''
Solution:
1) the idea is to iterate on set of first and on runtime: use string.count method on python to count the occurence of the specific char on string
2) if ever happens that the count of one is not equal of the count of the same char on next -> then we break by returning false
3) if reaches the end, return default True 
'''
