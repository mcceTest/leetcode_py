'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''
from pprint import pprint as pp


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        cached = {}

        for s in strs:
            sortedStr = ''.join(sorted(s))
            if sortedStr not in cached:
                cached[sortedStr] = []
            cached[sortedStr].append(s)

        return list(cached.values())
        


    @staticmethod
    def main():
        sol = Solution()

        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

        pp(sol.groupAnagrams(strs))
        

if __name__ == "__main__":
    Solution.main() 