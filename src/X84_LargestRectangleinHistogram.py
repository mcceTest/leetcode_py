'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10
'''

## TODO: use dp to find the left and right boundary

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        heights.append(-1)
        st = []
        res = 0
        for idx, height in enumerate(heights):
            while st and height <= heights[st[-1]]:
                cur = heights[st[-1]]
                st.pop()
                preIdx = -1
                if st:
                    preIdx = st[-1]

                res = max(res, cur * (idx - preIdx - 1))
            st.append(idx)

        

        return res

                


    @staticmethod
    def main():
        sol = Solution()
        height = [1]

        print(sol.largestRectangleArea(height))

        

if __name__ == "__main__":
    Solution.main() 