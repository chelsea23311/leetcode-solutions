# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
       
        p,q=list1,list2
        node=ListNode()
        cur=node
        while p is not None and q is not None:
            if p.val<=q.val:
                cur.next=p
                p=p.next
            else:
                cur.next=q
                q=q.next
            cur=cur.next
        if not p:
            cur.next=q
        else:
            cur.next=p
        return node.next
                
                
            
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        