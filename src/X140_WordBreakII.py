'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
'''


## NOTE: in dfs cache results to avoid redundent calculation
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not wordDict:
            return []
        # words = set(wordDict)
        preSteps = [ [] for _ in range(len(s) + 1)]

        # for startIdx in range(len(s)):
        #     for endIdx in range(startIdx + 1, len(s) + 1):
        #         if s[startIdx:endIdx] in words:
        #             preSteps[endIdx].append(startIdx)

        for startIdx in range(len(s)):
            for word in wordDict:
                endIdx = startIdx + len(word)
                if endIdx <= len(s) and s[startIdx:endIdx] == word:
                    preSteps[endIdx].append(startIdx)

        dp = [None] * (len(s) + 1)
        dp[0] = [[0]]
        res = self.dfs(s, len(s), preSteps, dp)

        result = []
        for curList in res:
            strList = []
            for i in range(len(curList) - 1):
                strList.append(s[curList[i]:curList[i+1]])
            result.append(' '.join(strList))

        return result


    def dfs(self, s, idx, preSteps, dp):
        if dp[idx] is not None:
            return dp[idx]

        res = []
        for preIdx in preSteps[idx]:
            for preRes in self.dfs(s, preIdx, preSteps, dp):
                tmp = preRes[:]
                tmp.append(idx)
                res.append(tmp)

        dp[idx] = res

        return res

        

    @staticmethod
    def main():
        sol = Solution()
        s =  "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

        wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        
        # s = "catsanddog"
        # wordDict = ["cat", "cats", "and", "sand", "dog"]
        
        print(sol.wordBreak(s, wordDict))


if __name__ == "__main__":
    Solution.main() 