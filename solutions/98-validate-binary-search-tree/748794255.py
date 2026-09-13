# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        output=[]
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            output.append(node.val)
            dfs(node.right)
        dfs(root)
        return all(output[i]<output[i+1] for i in range(len(output)-1))

                
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        