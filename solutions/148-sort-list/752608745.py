# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        deque=[]
        q=head
        while q is not None:
            deque.append(q)
            q=q.next
        deque.sort(key=lambda x:x.val)
        dummy=ListNode()
        cur=dummy
        for node in deque:
            cur.next=node
            cur=cur.next
        cur.next=None
        return dummy.next
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        