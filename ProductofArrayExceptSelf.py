'''
238. Product of Array Except Self - Medium
Given:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
'''
def productExceptSelf(self, nums):
        prefix_lst = [1] * len(nums)
        postfix_lst = [1] * len(nums)

        ans = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            prefix = prefix * nums[i]
            prefix_lst[i] = prefix

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix = postfix * nums[i]
            postfix_lst[i] = postfix

        ans[0] = postfix_lst[1]
        ans[-1] = prefix_lst[-2]

        for i in range(1, len(ans) - 1):
            ans[i] = prefix_lst[i - 1] * postfix_lst[i + 1]

        return ans

'''
Solution: 
1) the idea is two compute prefix multipilcation
2) compute the postfix multiplication 
3) then place the ans ans prefix[i-1] * postfix[I+1], so ut will be the same as multiplciation of all and divide it to current number
4) the edge case is the ans[0] and ans[-1], they are equal to postfix[1] and prefix[-2] since no pre and post for second, so only values of post and pre is taken

Time Complexity:  2 * O(N) -> O(N)
Space Complexity: 3 * O(N) -> O(N)
'''
