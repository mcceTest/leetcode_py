'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

## TODO: another approach
##          for each heigh, find the left max and right max, and the water above it would be:
##              min(leftMax, rightMax) - h
##          And the sum of all the water accumulated will be the total water
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0
        st = []
        res = 0
        for idx, h in enumerate(height):
            while st:
                topIdx = st[-1]
                if h >= height[topIdx]:
                    st.pop(-1)
                    if st:
                        leftHeight = height[st[-1]]
                        res += (min(leftHeight, h) - height[topIdx]) * (idx - st[-1] - 1)
                else:
                    break

            st.append(idx)

        return res


    @staticmethod
    def main():
        sol = Solution()

        height = [0,1,0,2,1,0,1,3,2,1,2,1]

        print(sol.trap(height))
        

if __name__ == "__main__":
    Solution.main()  

        
            