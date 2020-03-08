'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
  '''

from treeNode import TreeNode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## TODO: recurvise way

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        res = []
        cur = [root]

        while cur:
            res.append(cur[-1].val)
            nxt = []
            for node in cur:
                for nd in (node.left, node.right):
                    if nd is not None:
                        nxt.append(nd)
            cur = nxt
    
        return res
                       

        

    @staticmethod
    def main():
        sol = Solution()
        root = TreeNode.constructFromLevelList([1,2,3,None,5,None,4])
        print(sol.rightSideView(root))
        
        
if __name__ == "__main__":
    Solution.main()