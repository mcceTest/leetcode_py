'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
'''


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'

        isNeg = (numerator < 0) ^ (denominator < 0)
        res = ""
        if isNeg:
            res += '-'

        if numerator < 0:
            numerator *= -1

        if denominator < 0:
            denominator *= -1
        
        d = numerator // denominator
        res += str(d)
        numerator -= d * denominator
        if numerator == 0:
            return res

        res += '.'
        numerator *= 10
        startIdxMap = {}
        while numerator != 0:
            if numerator < denominator:
                res += '0'
                numerator *= 10
            else:
                if numerator in startIdxMap:
                    # found repeats
                    idx = startIdxMap[numerator]
                    res = res[:idx] + '(' + str(res[idx:]) + ')'
                    break
                else:
                    startIdxMap[numerator] = len(res)
                    cur = numerator // denominator
                    res += str(cur)
                    numerator -= cur * denominator
                    numerator *= 10

        return res


    @staticmethod
    def main():
        sol = Solution()
        numerator = 1
        denominator = 2
        print(sol.fractionToDecimal(numerator, denominator))

        
if __name__ == "__main__":
    Solution.main()