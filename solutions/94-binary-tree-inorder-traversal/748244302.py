# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def inorderTraversal(self, root):
        output=[]
        def visit(node):
            if not node:
                return
            visit(node.left)
            output.append(node.val)
            visit(node.right)
        visit(root)
        return output
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        