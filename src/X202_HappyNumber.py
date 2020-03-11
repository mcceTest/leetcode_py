'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''


## TODO: use two pointers to determine if there is a loop
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        found = set()
        while n not in found:
            if n == 1:
                return True

            found.add(n)
            n = self.nextN(n)

        return False


    def nextN(self, n):
        res = 0
        while n != 0:
            d = n % 10
            n = n // 10
            res += d * d

        return res
        

    @staticmethod
    def main():
        sol = Solution()
        
        n = 19
        print(sol.isHappy(n))
        
        
if __name__ == "__main__":
    Solution.main()