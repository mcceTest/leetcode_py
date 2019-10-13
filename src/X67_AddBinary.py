'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        aIdx = len(a) - 1
        bIdx = len(b) - 1

        res = []
        carry = 0
        while aIdx >= 0 or bIdx >= 0:
            aCur = '0'
            bCur = '0'
            if aIdx >= 0:
                aCur = a[aIdx]
                aIdx -= 1

            if bIdx >= 0:
                bCur = b[bIdx]
                bIdx -= 1

            if carry == 0:
                if aCur == '0':
                    res.append(bCur)
                elif bCur == '0':
                    res.append(aCur)
                else:
                    res.append('0')
                    carry = 1
            else:
                if aCur == '1':
                    carry = 1
                    res.append(bCur)
                elif bCur == '1':
                    carry = 1
                    res.append(aCur)
                else:
                    carry = 0
                    res.append('1')

        if carry == 1:
            res.append('1')

        res.reverse()

        return ''.join(res)
                    

    @staticmethod
    def main():
        sol = Solution()
        a = "11"
        b = "1"

        print(sol.addBinary(a, b))



if __name__ == "__main__":
    Solution.main() 

