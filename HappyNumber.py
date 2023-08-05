'''
202. Happy Number
Given:
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
Solution:
0) the important thing here is that if there is no one in the chain - > there is a cycle 
1) if even one, it hits cylce anyway
3) so we can track a set of visited node and use while loop to increment on the chain
4) at each increment -> add number(sum of squares) to visited
5) if loop 3 exited, means than cylce -> False
6) one exception, in loop 3, if n == 1, return True 
7) the function for sumOfSquares is calculatated by while loop and n % 10, then square it and add it to output,
then n = n // 10 to get rid of last digit, 121 -> 12 -> 1 (+=1^2  -> +=2 ^ 2 ->+=1^ 2)  
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False

    def sumOfSquares(self, n):
        summa = 0 

        while n:
            digit = n % 10
            summa += digit ** 2
            n = n // 10  

        return summa 
