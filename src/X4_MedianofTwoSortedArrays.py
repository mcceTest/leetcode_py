'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1:
            return self.medianOfOneArray(nums2)

        if not nums2:
            return self.medianOfOneArray(nums1)

        slist = None
        llist = None
        if len(nums1) > len(nums2):
            slist, llist = nums2, nums1
        else:
            slist, llist = nums1, nums2

        totalLen = len(nums1) + len(nums2)

        if totalLen % 2 == 1:
            if slist[0] >= llist[len(llist) - 1]:
                return llist[totalLen // 2]

            if llist[0] >= slist[len(slist) - 1]:
                return llist[totalLen // 2 - len(slist)]

            sLow = 0
            sHigh = len(slist) - 1
            
            while sLow <= sHigh:
                sIdx = (sLow + sHigh) // 2
                lIdx = totalLen // 2 - 1 - sIdx
                if llist[lIdx] >= slist[sIdx]:
                    if sIdx == len(slist) -1 or llist[lIdx] <= slist[sIdx+1]:
                        return llist[lIdx]
                    else:
                        sLow = sIdx + 1
                else:
                    if lIdx == len(llist) - 1 or slist[sIdx] <= llist[lIdx+1]:
                        return slist[sIdx]
                    else:
                        sHigh = sIdx - 1

            if sHigh < 0:
                return llist[lIdx+1]
        else:
            if slist[0] >= llist[len(llist) - 1]:
                if len(slist) == len(llist):
                    return (slist[0] + llist[len(llist) - 1]) / 2
                else:
                    return (llist[totalLen // 2 - 1] + llist[totalLen // 2]) / 2

            if llist[0] >= slist[len(slist) - 1]:
                if len(slist) == len(llist):
                    return (slist[len(slist) - 1] + llist[0]) / 2
                else:
                    return (llist[totalLen // 2 - 1 - len(slist)] + llist[totalLen // 2 - len(slist)]) / 2

            sLow = 0
            sHigh = len(slist) - 1
            
            while sLow <= sHigh:
                sIdx = (sLow + sHigh) // 2
                lIdx = totalLen // 2 - 1 - sIdx

                if llist[lIdx] >= slist[sIdx]:
                    if sIdx == len(slist) -1 or llist[lIdx] <= slist[sIdx+1]:
                        if lIdx == 0 or slist[sIdx] >= llist[lIdx-1]:
                            return (llist[lIdx] + slist[sIdx]) / 2
                        else:
                            return (llist[lIdx] + llist[lIdx-1]) / 2
                    else:
                        sLow = sIdx + 1
                else:
                    if lIdx == len(llist) - 1 or slist[sIdx] <= llist[lIdx+1]:
                        if sIdx == 0 or llist[lIdx] >= slist[sIdx-1]:
                            return (llist[lIdx] + slist[sIdx]) / 2
                        else:
                            return (slist[sIdx] + slist[sIdx-1]) / 2
                    else:
                        sHigh = sIdx - 1

            if sHigh < 0:
                return (llist[lIdx] + llist[lIdx+1]) / 2

    def medianOfOneArray(self, nums):
        if not nums:
            return 0

        if len(nums) % 2 == 1:
            return nums[len(nums) // 2]
        else:
            return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2


    @staticmethod
    def main():
        sol = Solution()

        print(sol.findMedianSortedArrays([4], [1, 2, 3]))


if __name__ == "__main__":
    Solution.main()     

