'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        cached = [0] * (len(s) + 1)
        cached[len(s)] = 1

        for idx in range(len(s) - 1, -1, -1):
            if s[idx] == '0':
                cached[idx] = 0
            elif s[idx] == '1':
                if idx == len(s) - 1:
                    cached[idx] = 1
                else:
                    cached[idx] = cached[idx + 1] + cached[idx + 2]
            elif s[idx] == '2':
                if idx == len(s) - 1:
                    cached[idx] = 1
                else:
                    if s[idx + 1] > '6':
                        cached[idx] = cached[idx + 1]
                    else:
                        cached[idx] = cached[idx + 1] + cached[idx + 2]
            else:
                cached[idx] = cached[idx + 1]

        return cached[0]


    @staticmethod
    def main():
        sol = Solution()
        s = '12'

        print(sol.numDecodings(s))

        

if __name__ == "__main__":
    Solution.main() 
            