'''
80. Remove Duplicates from Sorted Array II - Medium
Given:
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''
'''
Solution:
The idea is to start l, r at 0
0) while r < len(nums) condition:
1) then iterate r while old number persist 
2) then count how many iteration r pointer made
3) if r made > 2 more iteration, need to add only two, if less, only one substitution, then left pointer is iterated one more
4) finally r pointer iterated once to start the 1) again 
'''

def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        while r < len(nums):
            count = 1 
            while r + 1 <= len(nums) - 1 and nums[r] == nums[r + 1]:
                r += 1
                count += 1

            if count >= 2:
                for i in range(2):
                    nums[l] = nums[r]
                    l+= 1
            else:
                nums[l] = nums[r]
                l+= 1
            
            # for i in range(min(count ,2)):
            #     nums[l] = nums[r]
            #     l += 1
            
            r += 1
        
        return l
