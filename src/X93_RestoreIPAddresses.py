'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''


class Solution(object):
    def restoreIpAddresses2(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4 or len(s) > 12:
            return []

        res = []
        cur = []

        self.dfs(s, 0, 0, cur, res)

        result = self.norm(s, res)

        return result


    def dfs(self, s, parts, idx, cur, res):
        if idx == len(s):
            if parts == 4:
                res.append(cur[:])
            return

        if parts == 4:
            return

        cur.append(idx)
        self.dfs(s, parts + 1, idx + 1, cur, res)
        cur.pop()

        if s[idx] != '0' and idx < len(s) - 1:
            cur.append(idx)
            self.dfs(s, parts + 1, idx + 2, cur, res)
            cur.pop()

            if idx < len(s) - 2 and int(s[idx:idx + 3]) < 256:
                cur.append(idx)
                self.dfs(s, parts + 1, idx + 3, cur, res)
                cur.pop()


    def norm(self, s, res):
        result = []
        for cur in res:
            curStr = ''
            for i in range(3):
                curStr += (s[cur[i]:(cur[i + 1])] + '.')
            curStr += s[cur[3]:len(s)]

            result.append(curStr)

        return result


    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4 or len(s) > 12:
            return []

        res = []
        
        start1 = 0
        maxEnd1 = self.getMaxEnd(s, start1)
        if maxEnd1 is not None:
            for end1 in range(1, maxEnd1 + 1):
                s1 = s[:end1]
                if not self.isValid(s1): continue
                start2 = end1
                maxEnd2 = self.getMaxEnd(s, start2)
                if maxEnd2 is not None:
                    for end2 in range(start2 + 1, maxEnd2 + 1):
                        s2 = s[start2:end2]
                        if not self.isValid(s2): continue
                        start3 = end2
                        maxEnd3 = self.getMaxEnd(s, start3)
                        if maxEnd3 is not None:
                            for end3 in range(start3 + 1, maxEnd3 + 1):
                                s3 = s[start3:end3]
                                if not self.isValid(s3): continue

                                start4 = end3
                                if start4 >= len(s) or start4 < len(s) - 3: continue
                                s4 = s[start4:]
                                if not self.isValid(s4): continue

                                res.append('.'.join([s1, s2, s3, s4]))

        return res

    def isValid(self, s):
        if s[0] == '0':
            return len(s) == 1
        else:
            return int(s) < 256

    def getMaxEnd(self, s, start):
        if start >= len(s):
            return None

        if s[start] == '0':
            return start + 1
        else:
            return min(start + 3, len(s))


    @staticmethod
    def main():
        sol = Solution()
        s = "25525511135"

        print(sol.restoreIpAddresses(s))
        

if __name__ == "__main__":
    Solution.main() 

        


        
