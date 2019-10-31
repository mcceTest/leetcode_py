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

        return self.isScrambleHelper(s1, s2, 0, len(s1) - 1, 0, len(s2) - 1)


    def isScrambleHelper(self, s1, s2, start1, end1, start2, end2):
        l = end1 - start1 + 1
        if l <= 0:
            return True

        if l == 1:
            return s1[start1] == s2[start2]
        else:
            for i in range(l - 1):
                if self.isScrambleHelper(s1, s2, start1, start1 + i, start2, start2 + i) and self.isScrambleHelper(s1, s2, start1 + i + 1, end1, start2 + i + 1, end2):
                    return True

                if self.isScrambleHelper(s1, s2, start1, start1 + i, end2 - i, end2) and self.isScrambleHelper(s1, s2, start1 + i + 1, end1, start2, end2 - i - 1):
                    return True

        return False     

    @staticmethod
    def main():
        sol = Solution()
        s1 = "abcdefghijklmnopq"
        s2 = "efghijklmnopqcadb"
        print(sol.isScramble(s1, s2))

        

if __name__ == "__main__":
    Solution.main() 