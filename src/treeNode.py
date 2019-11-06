class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def constructFromLevelList(lst):
        if not lst or (lst[0] is None):
            return None

        root = TreeNode(lst[0])
        preNodes = [root]
        curNodes = []

        curIdx = 1

        while True:
            curNodes = []
            for node in preNodes:
                if curIdx < len(lst):
                    curNode = lst[curIdx]
                    if curNode is not None:
                        tmpNode = TreeNode(curNode)
                        curNodes.append(tmpNode)
                        node.left = tmpNode
                    curIdx += 1
                else:
                    return root
                
                if curIdx < len(lst):
                    curNode = lst[curIdx]
                    if curNode is not None:
                        tmpNode = TreeNode(curNode)
                        curNodes.append(tmpNode)
                        node.right = tmpNode
                    curIdx += 1
                else:
                    return root

            preNodes = curNodes

        return root

    @staticmethod
    def toList(node):
        if node is None:
            return [None]
        cur = node
        preNodes = [cur]

        res = []
        while preNodes:
            curNodes = []
            for n in preNodes:
                if n is None:
                    res.append(None)
                else:
                    res.append(n.val)
                    curNodes.append(n.left)/
                    curNodes.append(n.right)

            while curNodes and curNodes[-1] is None:
                curNodes.pop()

            preNodes = curNodes

        return res

    def __repr__(self):
        return TreeNode.toList(self)

    