'''
49. Group Anagrams - Medium
Given:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
def keyword(self, word):
        return ''.join(sorted(word))
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            groupkey = self.keyword(word)
            if groupkey not in groups:
                groups[groupkey] = []
            groups[groupkey].append(word)

        res = [] 
        for key in groups:
            res.append(groups[key])
        return res 

'''
Solution:
1) the idea is iterate and sort the str, this str is a key of the group 
2) then add all the same key strings to this group 
3) then iterate on the hashmap and append all list values to one res list 
'''
