'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

'''

from treeNode import TreeNode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None

        inorderIdx = {}
        for i, v in enumerate(inorder):
            inorderIdx[v] = i

        return self.bt(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1, inorderIdx)


    def bt(self, preorder, inorder, pstart, pend, istart, iend, inorderIdx):
        if pstart > pend:
            return None

        node = TreeNode(preorder[pstart])
        
        inIdx = inorderIdx[node.val]
        leftSubNum = inIdx - istart
        node.left = self.bt(preorder, inorder, pstart + 1, pstart + leftSubNum, istart, inIdx - 1, inorderIdx)
        node.right = self.bt(preorder, inorder, pstart + leftSubNum + 1, pend, inIdx + 1, iend, inorderIdx)

        return node

    @staticmethod
    def main():
        sol = Solution()
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        node = sol.buildTree(preorder, inorder)
        print(TreeNode.toList(node))

if __name__ == "__main__":
    Solution.main() 