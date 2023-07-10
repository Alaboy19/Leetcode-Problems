'''
131. Palindrome Partitioning
Given:
Given a string s, partition s such that every substring
of the partition is a palindrome. Return all possible palindrome partitioning of s.
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Solution:
The idea is to use slide pointer, aab -> a(Pal) -> check(a) (pal) -> check(b)
                  aab
                /    |   \
              a    aa  ab
             /       |    not good
           a        b
          /        good
         b
        good
1) base case when i over the length of string
1) from for j in range(i, len), check if s[i:j+1] is pal:
if pal, append it and do  dfs on j+1
2) else, we track path and append all the palindromes, if not palindrome,  keep on iterataive
3) if palindrome, append and recursively deep in from next element 
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res =[]
        def isPalindrome(string):
            ptr1, ptr2 = 0, len(string) - 1
            while ptr1 < ptr2:
                if string[ptr1] != string[ptr2]:
                    return False 
                ptr1, ptr2 = ptr1 + 1, ptr2 - 1
            return True

        def dfs(i, path):
            if i >= len(s):
                res.append(path.copy())
                return 

            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    path.append(s[i:j+1])
                    dfs(j+1, path)
                    path.pop()

        dfs(0, [])
        return res
