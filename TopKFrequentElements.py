'''
347. Top K Frequent Elements - Medium 
Given: 
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_val_occ = {}
        for num in nums:
            count_val_occ[num] = 1 + count_val_occ.get(num, 0)
        
        count_freq = [[] for i in range(len(nums) + 1)]

        for val, occ in count_val_occ.items():
            count_freq[occ].append(val)

        ans = []

        for i in range(len(count_freq) - 1 , 0, -1):
            for n in count_freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans

'''
Solution:

'''
