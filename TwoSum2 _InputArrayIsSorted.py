'''
167. Two Sum II - Input Array Is Sorted
Given:
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.
Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Two Sum II - Input Array Is Sorted
'''
'''
Solution:
1) assign left and right pointer to 0, len(nums) - 1
2) since the array is sorted initially, we can iterate left ptr to right if summa is less
3) and iterate right ptr to left if summa is higher 
5) we are garanteed to be given a case with one exact solution 
''',
def twoSum(self, numbers: List[int], target: int) -> List[int]:
        fst_ptr, snd_ptr = 0, len(numbers) - 1
        while snd_ptr >= fst_ptr:
            summa = numbers[fst_ptr] + numbers[snd_ptr]
            if summa == target:
                return [fst_ptr + 1, snd_ptr + 1]
            elif summa > target:
                snd_ptr -= 1
            else:
                fst_ptr += 1
