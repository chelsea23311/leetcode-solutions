# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def maxPathSum(self, root):
        self.maxnum = float('-inf')
        def dfs(node):
            if not node:
                return 0
            left_sum=dfs(node.left)
            right_sum=dfs(node.right)
            candidate = max( left_sum + node.val, right_sum + node.val, left_sum + node.val + right_sum, node.val )
            if candidate > self.maxnum:
                self.maxnum = candidate
            return max(left_sum+node.val,right_sum+node.val,node.val)
        dfs(root)
        return self.maxnum
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        