'''
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
'''

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = list(range(1, n + 1))
        cached = [1] * n
        for i in range(2, n):
            cached[i] = cached[i - 1] * i

        res = ''
        k -= 1
        for i in range(n - 1, -1, -1):
            if k == 0:
                for num in nums:
                    res += str(num)
                break
            else:
                cur = k // cached[i]
                res += str(nums[cur])
                nums.pop(cur)
                k -= cur * cached[i]

        return res

    @staticmethod
    def main():
        sol = Solution()
        n = 2
        k = 2
        print(sol.getPermutation(n, k))

if __name__ == "__main__":
    Solution.main() 