'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
'''
## TODO: constant space solution

from treeNode import TreeNode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        st = []
        cur = root
        inorder = []
        
        while st or cur is not None:
            while cur is not None:
                st.append(cur)
                cur = cur.left

            top = st[-1]
            st.pop()
            
            inorder.append(top)
            cur = top.right

        leftIdx = -1
        for idx in range(len(inorder) - 1):
            if inorder[idx].val > inorder[idx + 1].val:
                leftIdx = idx
                break

        rightIdx = -1
        for idx in range(len(inorder) - 1, 0, -1):
            if inorder[idx].val < inorder[idx - 1].val:
                rightIdx = idx
                break

        inorder[leftIdx].val, inorder[rightIdx].val = inorder[rightIdx].val, inorder[leftIdx].val

        return


    @staticmethod
    def main():
        sol = Solution()
        root = TreeNode.constructFromLevelList([1,3,None, None,2])
        sol.recoverTree(root)
        print(root)

if __name__ == "__main__":
    Solution.main() 

