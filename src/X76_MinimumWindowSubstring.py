'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        tLen = len(t)
        if tLen == 0 or len(s) == 0 or tLen > len(s):
            return ''

        tMap = {}
        for c in t:
            tMap[c] = tMap.get(c, 0) + 1

        startIdx = 0
        curIdx = 0
        count = 0
        minStartIdx = 0
        minLen = len(s) + 1

        while curIdx < len(s):
            c = s[curIdx]
            if c in tMap:
                tMap[c] = tMap[c] - 1
                if tMap[c] >= 0:
                    count += 1
                    if count == len(t):
                        while True:
                            sCur = s[startIdx]
                            if sCur in tMap:
                                tMap[sCur] += 1
                                if tMap[sCur] > 0:
                                    count -= 1
                                    break
                            startIdx += 1
                        curLen = curIdx - startIdx + 1
                        if curLen < minLen:
                            minLen = curLen
                            minStartIdx = startIdx
                        startIdx += 1
            curIdx += 1

        if minLen < len(s) + 1:
            return s[minStartIdx:(minStartIdx + minLen)]
        else:
            return ''


    @staticmethod
    def main():
        sol = Solution()
        S = "ADOBECODEBANC"
        T = "ABC"
        print(sol.minWindow(S, T))

if __name__ == "__main__":
    Solution.main()   

                

