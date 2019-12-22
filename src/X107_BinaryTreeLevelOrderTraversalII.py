'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''


from treeNode import TreeNode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        res = []
        q = Queue()
        q.put(root)

        while not q.empty():
            qs = q.qsize()
            curValues = []
            for _ in  range(qs):
                node = q.get()
                curValues.append(node.val)
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
            res.insert(0, curValues)

        return res

    @staticmethod
    def main():
        sol = Solution()
        root = TreeNode.constructFromLevelList([3,9,20,None,None,15,7])
        print(sol.levelOrderBottom(root))

if __name__ == "__main__":
    Solution.main() 