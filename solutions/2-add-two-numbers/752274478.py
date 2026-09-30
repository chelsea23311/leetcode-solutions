# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        nodes=ListNode()
        cur=nodes
        p,q=l1,l2
        forward=0
        while p is not None or q is not None:
            if not p:
                sum=q.val+forward
            elif not q:
                sum=p.val+forward
            else:
                sum=p.val+q.val+forward
            if sum>=10:
                forward=1
                sum=sum%10
            else:
                forward=0
            node=ListNode(sum)
            cur.next=node
            cur=cur.next
            p=p.next if p is not None else p
            q=q.next if q is not None else q
        if forward==1:
            node=ListNode(1)
            cur.next=node
        return nodes.next
        
       

        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        