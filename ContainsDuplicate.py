'''
Given:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''
def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
'''
1) the idea is very simple
2) we use hashset to store the seen elements while iterating
3) we check whether it contains already in seen -> if yes -> return True, if not -> keep going and add this num in seen
4) return defult False value if iteration reaches the end -> which means no duplate met 
'''
