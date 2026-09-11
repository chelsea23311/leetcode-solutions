# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        output=[]
        if not root:
            return output
        quene=[root]
        def bfs():
            while len(quene)!=0:
                level_size=len(quene)
                level_val=[]
                for _ in range(level_size):
                    q=quene.pop(0)
                    level_val.append(q.val)
                    if q.left:
                        quene.append(q.left)
                    if q.right:
                        quene.append(q.right)
                output.append(level_val)
        bfs()
        return output
           
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        