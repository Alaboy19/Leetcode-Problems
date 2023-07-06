'''
128. Longest Consecutive Sequence - Medium
Given:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time
'''
def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest = 0 

        
        for num in nums:

            if not (num - 1) in my_set:
                count = 1
                while (num + count) in my_set:
                    count += 1
                longest = max(count, longest)

        return longest

'''
Solution:
The overall idea is to check for every element whether its next consequetive sequence presents in the array and track the max for every num 
1) in order to have o(1) check, we need to convert the array to set, set is because get rid of duplicates
2) so we iterate and check wether the number is start of sequence by (if not (num-1) in set:)
3) then start with it by count = 1(it has itself), then while(num + count) in set:
count += 1
4) then just update our ans with max(count, ans)
'''
