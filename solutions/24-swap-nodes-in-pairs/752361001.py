# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        p=head
        nodes=ListNode()
        cur=nodes
        nodes.next=head
        while p is not None and p.next is not None:
            
            q=p.next
            p_before=p
            cur.next=q
            p=q.next
            q.next=p_before
            cur=p_before
        cur.next=p
        return nodes.next

        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        