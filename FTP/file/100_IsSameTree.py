# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # decide whether p q exists
        if p is None and q is None:
            return True
        if not (p and q):
            return False
        else:
            left_same = self.isSameTree(p.left,q.left)
            right_same = self.isSameTree(p.right,q.right)
            return p.val == q.val and left_same and right_same
