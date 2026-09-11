# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.count=0
        def dfs(node):
            if not node:
                return 0
            left_count=dfs(node.left)
            right_count=dfs(node.right)
            if left_count+right_count>self.count:
                self.count=left_count+right_count
            return max(left_count,right_count)+1
        dfs(root)
        return self.count

        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        