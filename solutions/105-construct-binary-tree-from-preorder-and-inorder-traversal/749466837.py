# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        def dfs(node_val,flag_left,flag_right):
            idx=inorder.index(node_val)
            left_count=idx-flag_left
            right_count=flag_right-idx
            left_index=preorder.index(node_val)
            node=TreeNode(node_val,None,None)
            if left_count!=0:
                node.left=dfs(preorder[left_index+1],flag_left,idx-1)
            if right_count!=0:
                node.right=dfs(preorder[left_index+left_count+1],idx+1,flag_right)
            return node
        return dfs(preorder[0],0,len(preorder)-1)
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        