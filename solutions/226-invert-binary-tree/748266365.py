# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        def visit(node):
            if not node or (not node.left and not node.right):
                return
            visit(node.left)
            visit(node.right)
            invert_node=node.left
            node.left=node.right
            node.right=invert_node
        visit(root)
        return root
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        