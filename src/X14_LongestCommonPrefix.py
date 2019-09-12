'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""

        minLen = min(map(lambda x: len(x), strs))

        res = ""
        for i in range(minLen):
            c = strs[0][i]
            allFound = True
            for s in strs:
                if s[i] != c:
                    allFound = False
                    break
            
            if allFound:
                res += c
            else:
                break

        return res


    @staticmethod
    def main():
        sol = Solution()

        print(sol.longestCommonPrefix(["flower","flow","flight"]))

        
if __name__ == "__main__":
    Solution.main()   