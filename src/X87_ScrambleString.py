'''
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
'''

## TODO: for each substr, count number of chars first

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True

        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False

        cached = [ [ [ None ] * len(s1) for _ in range(len(s1))] for _ in range(len(s1))]
        return self.isScrambleHelper(s1, s2, 0, 0, len(s1), cached)


    def isScrambleHelper(self, s1, s2, start1, start2, sLen, cached):
        if sLen <= 0:
            return True

        if cached[start1][start2][sLen - 1] is not None:
            return cached[start1][start2][sLen - 1]

        res = False

        if sLen == 1:
            if s1[start1] == s2[start2]:
                res = True
        else:
            for i in range(1, sLen):
                if self.isScrambleHelper(s1, s2, start1, start2, i, cached) and self.isScrambleHelper(s1, s2, start1 + i, start2 + i, sLen - i, cached):
                    res = True
                    break

                if self.isScrambleHelper(s1, s2, start1, start2 + (sLen - i), i, cached) and self.isScrambleHelper(s1, s2, start1 + i, start2, sLen - i, cached):
                    res = True
                    break

        cached[start1][start2][sLen - 1] = res

        return res     

    @staticmethod
    def main():
        sol = Solution()
        s1 = "abcdefghijklmnopq"
        s2 = "efghijklmnopqcadb"

        s1 = "great"
        s2 = "rgeat"
        
        print(sol.isScramble(s1, s2))

        

if __name__ == "__main__":
    Solution.main() 