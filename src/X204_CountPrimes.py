'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        primeFlag = [True] * n
        count = 0
        cur = 2
        while cur < n:
            count += 1
            times = 2
            curProd = cur * times
            while curProd < n:
                primeFlag[curProd] = False
                times += 1
                curProd = cur * times
            
            nxt = cur + 1
            while nxt < n and not primeFlag[nxt]:
                nxt += 1
            cur = nxt

        return count
        

    @staticmethod
    def main():
        sol = Solution()
        n = 10
        print(sol.countPrimes(n))
        
        
if __name__ == "__main__":
    Solution.main()