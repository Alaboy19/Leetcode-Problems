'''
1. Two Sum
Given:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''
def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp2idx = {}
        for i in range(len(nums)):
            if nums[i] in comp2idx:
                return comp2idx[nums[i]], i
            comp2idx[target - nums[i]] = i

'''
Solution:
1) the idea is to iterate and write the complement and its idx on hashpmap
2) when iterating, look from hashmap, whether this num in wanted and prevoius seen compelement and its idx, return prev_idx, current_idx
3) since there is a gurantee that it has one solution we do not return defaultly
'''
