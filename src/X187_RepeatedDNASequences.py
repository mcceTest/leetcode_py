'''
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
'''



class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        countMap = {}
        res = []
        for i in range(0, len(s) - 9):
            cur = s[i:(i+10)]
            if cur not in countMap:
                countMap[cur] = 1
            else:
                countMap[cur] += 1

        for k, v in countMap.items():
            if v >= 2:
                res.append(k)

        return res
        


    @staticmethod
    def main():
        sol = Solution()
        s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        print(sol.findRepeatedDnaSequences(s))
        
        
if __name__ == "__main__":
    Solution.main()