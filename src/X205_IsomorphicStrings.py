'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
'''



## TODO: number of counts of corresponding chars in s and t have to be the same at each step
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        sd = {}
        td = {}
        for i in range(len(s)):
            si = s[i]
            ti = t[i]

            if si not in sd:
                if ti in td:
                    return False
                else:
                    sd[si] = ti
                    td[ti] = si
            else:
                if sd[si] != ti:
                    return False

        return True


    @staticmethod
    def main():
        sol = Solution()
        s = "egg"
        t = "add"
        print(sol.isIsomorphic(s, t))
        
if __name__ == "__main__":
    Solution.main()