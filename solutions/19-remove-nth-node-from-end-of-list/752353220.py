# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        p,q=head,head
        for _ in range(n):
            q=q.next
        while q is not None:
            q=q.next
            p=p.next
        nodes=ListNode()
        nodes.next=head
        cur=nodes
       
        while cur.next!=p:
            cur=cur.next
        cur.next=p.next
        return nodes.next

        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        