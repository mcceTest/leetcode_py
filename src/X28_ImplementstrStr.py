'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''


class Solution(object):
    def strStr2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        if not haystack:
            return -1

        for idx in range(len(haystack) - len(needle) + 1):
            isMatch = True
            for pIdx in range(len(needle)):
                if haystack[idx + pIdx] != needle[pIdx]:
                    isMatch = False
                    break
            if isMatch:
                return idx
            
        return -1


    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        if not haystack:
            return -1

        lps = self._preprocess(needle)
        print(lps)

        pLen = len(needle)
        pIdx = 0
        sIdx = 0

        while sIdx <= len(haystack):
            if pIdx == pLen:
                return sIdx - pLen
            elif sIdx == len(haystack):
                break
            else:
                if haystack[sIdx] == needle[pIdx]:
                    sIdx += 1
                    pIdx += 1
                else:
                    if pIdx == 0:
                        sIdx += 1
                    else:
                        pIdx = lps[pIdx - 1]

        return -1


    def _preprocess(self, p):
        if not p:
            return None

        res = [0] * len(p)

        for idx in range(1, len(p)):
            preLen = res[idx - 1]

            while preLen != 0 and p[preLen] != p[idx]:
                preLen = res[preLen - 1]

            if p[preLen] == p[idx]:
                res[idx] = preLen + 1
            
        return res

    @staticmethod
    def main():
        sol = Solution()

        haystack = "a"
        needle = "a"
        
        print(sol.strStr(haystack, needle))


if __name__ == "__main__":
    Solution.main()   