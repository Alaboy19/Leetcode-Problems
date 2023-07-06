'''
Given:
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
'''
'''
Solution:
1) create Hashmap and write inside the num to idx mapping 
2) check if num in hashmap and diff with k, if yes -> return true
3) if not, just whether condition met or not(can replace old value), update num - idx
4) continue checking
5) looped over and nothing, return False 
'''
def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen_indices = {}

        for idx, num in enumerate(nums):
            if num in seen_indices and idx - seen_indices[num] <= k:
                return True

            seen_indices[num] = idx

        return False
