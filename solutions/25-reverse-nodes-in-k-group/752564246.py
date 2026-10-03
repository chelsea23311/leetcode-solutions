# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        
        count=0
        dummy=ListNode()
        cur=dummy
        cur.next=head
        q=head
        while q is not None:
            q=q.next
            count+=1
        while count-k>=0:
            q=cur.next
            nodes=q.next
            for _ in range(k-1):
                p=nodes
                nodes=p.next
                p.next=q
                q=p
            cur.next.next=nodes
            forward=cur.next
            cur.next=q
            cur=forward
            
            count-=k
        return dummy.next





        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        