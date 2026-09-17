# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node):
            if not node:
                return None
            if p==node or q==node :
                return node
            left=dfs(node.left)
            right=dfs(node.right)
            if left and right:
                return node
            if left:
                return left
            if right:
                return right
        return dfs(root)




        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        