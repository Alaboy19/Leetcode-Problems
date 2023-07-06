'''
Given:
11. Container With Most Water - Medium
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
'''
'''
Solution:
1) the overall idea is to measure area with two pointer and start from 0, len(nums) - 1
2) then update the area with max
3) the condition to iterate is to iterate the pointer with less height, so most hight will stay 
'''

def maxArea(self, numbers: List[int]) -> int:
        ans_area = 0
        str_ptr, end_ptr = 0, len(numbers) - 1

        while str_ptr < end_ptr:
            area = (end_ptr - str_ptr) * min(numbers[str_ptr], numbers[end_ptr])
            ans_area = max(ans_area, area)
            if numbers[str_ptr] <= numbers[end_ptr]:
                str_ptr += 1
            else:
                end_ptr -= 1
        return ans_area
