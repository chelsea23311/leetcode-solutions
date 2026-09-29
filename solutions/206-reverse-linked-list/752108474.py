# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        deque=[]
       
        while head is not None:
            deque.append(head)
            head=head.next
        if not deque:
            return None
        q=deque.pop(-1)
        root=q
        while deque:
            p=deque.pop(-1)
            p.next=None
            q.next=p
            q=p
        return root
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        