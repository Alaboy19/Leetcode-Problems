'''
Given:
739. Daily Temperatures
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
'''
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for idx, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                ans[stack[-1][1]] = idx - stack[-1][1]
                stack.pop()
            stack.append([val, idx])

        return ans
