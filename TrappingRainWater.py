'''
Given:
42. Trapping Rain Water - Hard
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
'''
'''
Solution:
0) funny name of strategy - claim from both side and collect water one by one (means idx-wise)
1) the idea is to find the max height and work in two directions, from left to height, from right to height
2) so, iterate from left and the water is prevented from leaking because of wall staying to left to it, so if h[wall] > h[current], water += h[wall] - h[current]
3) if not the case, then current become a new_wall, since it is taller than before wall, and current  = current + 1
4) this 2-3 goes until current < max height idx
5) do the same with from right side to max_height
'''
def trap(self, numbers: List[int]) -> int:
        max_point = max(numbers)
        max_idx = 0
        for idx in range(len(numbers)):
            if numbers[idx] == max_point:
                max_idx = idx

        trap_area = 0

        wall_idx = 0
        current_idx = wall_idx + 1
        while current_idx < max_idx:
            if numbers[current_idx] < numbers[wall_idx]:
                trap_area += numbers[wall_idx] - numbers[current_idx]
                current_idx += 1
            else:
                wall_idx = current_idx
                current_idx = wall_idx + 1

        wall_idx = len(numbers) - 1
        current_idx = wall_idx - 1
        while current_idx > max_idx:
            if numbers[current_idx] < numbers[wall_idx]:
                trap_area += numbers[wall_idx] - numbers[current_idx]
                current_idx -= 1
            else:
                wall_idx = current_idx
                current_idx = wall_idx - 1

        return trap_area
