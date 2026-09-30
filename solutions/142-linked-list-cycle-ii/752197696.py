# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        nodes=set()
        node=head
        while node is not None:
            if node in nodes:
                return node
            else:
                nodes.add(node)
                node=node.next
        return None
        """
        :type head: ListNode
        :rtype: ListNode
        """
        