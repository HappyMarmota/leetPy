class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        arrnum = self.getNodeNum(root, 0)
        sumnum = 0
        for val in arrnum:
            sumnum = sumnum + val
        return sumnum

    def getNodeNum(self, node: TreeNode, val: int):
        if node is None:
            return None
        if node.left is None and node.right is None:
            res = val + node.val
            return [res]

        arrNum = []
        val = val + node.val
        if node.left is not None:
            arrNum.extend(self.getNodeNum(node.left, val*10))
        if node.right is not None:
            arrNum.extend(self.getNodeNum(node.right, val*10))
        return arrNum
