'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
 '''


from listNode import ListNode
 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from treeNode import TreeNode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nNodes = 0
        nodeIdx = {}
        cur = head
        while cur is not None:
            nodeIdx[nNodes] = cur
            nNodes += 1
            cur = cur.next

        return self.bt(0, nNodes - 1, nodeIdx)

    def bt(self, istart, iend, nodeIdx):
        if istart > iend:
            return None

        mid = (istart + iend) // 2
        node = TreeNode(nodeIdx[mid].val)

        node.left = self.bt(istart, mid - 1, nodeIdx)
        node.right = self.bt(mid + 1, iend, nodeIdx)

        return node
        
        

    @staticmethod
    def main():
        sol = Solution()
        head = ListNode.constructFromList([-10,-3,0,5,9])
        root = sol.sortedListToBST(head)

        print(TreeNode.toList(root))

if __name__ == "__main__":
    Solution.main() 