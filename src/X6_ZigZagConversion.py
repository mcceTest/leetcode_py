'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # one line, which is special case
        if numRows == 1:
            return s

        res = []
        for row in range(numRows):
            rowRes = self.convertRow(s, row, numRows)
            if rowRes:
                res.extend(rowRes)
            else:
                break
        
        return ''.join(res)

    
    def convertRow(self, s, row, numRows):
        res = []

        curIdx = row
        while curIdx < len(s):
            res.append(s[curIdx])
            
            if row == 0 or row == (numRows - 1):
                curIdx += (numRows - 1) * 2
            else:
                curIdx += (numRows - 1 - row) * 2
                if curIdx < len(s):
                    res.append(s[curIdx])
                    curIdx += row * 2
                else:
                    break

        return res


    @staticmethod
    def main():
        sol = Solution()

        print(sol.convert("PAYPALISHIRING", 3))

        print(sol.convert("PAYPALISHIRING", 4))

        print(sol.convert("A", 1))



if __name__ == "__main__":
    Solution.main()