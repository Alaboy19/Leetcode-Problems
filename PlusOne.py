'''
66. Plus One
Given:
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
Solution:
0) the first thing is to reverse the list
1) then make carry as one and init to 1
2) while carry is 1: i++
3) and i < len(digits): if digit[i] =9-> digit[0] -> carry stays the same as 1
4) else digits[i] += 1 and break or carry = 0 
5) when i >=len, digits.append(0), in case 9999 + 1, then break or carry = 0 
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]

        one, i = 1, 0

        while one == 1:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                    one = 1
                else:
                    digits[i] += 1
                    break 
            else:
                digits.append(one)
                break 
            
            i += 1

        return digits[::-1]
