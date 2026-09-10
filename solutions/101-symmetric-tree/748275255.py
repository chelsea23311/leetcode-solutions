# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def dfs(left,right):
            if not left and not right:
                return True
            if (not left or not right) or left.val!=right.val :
                return False
            if dfs(left.right,right.left) and dfs(left.left,right.right):
                return True
        if dfs(root.left,root.right):
            return True
        else:
            return False
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        