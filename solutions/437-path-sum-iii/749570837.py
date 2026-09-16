# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        self.count=0
        
        def dfs(node,sum):
            if not node:
                return
            sum+=node.val
            if sum==targetSum:
                self.count+=1
            dfs(node.left,sum)
            dfs(node.right,sum)
            
        def circle(node):
            if not node:
                return
            dfs(node,0)
            circle(node.left)
            circle(node.right)
        circle(root)
        return self.count
           
            

        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        