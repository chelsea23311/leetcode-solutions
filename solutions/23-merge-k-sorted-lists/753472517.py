# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        def merge_two(l1,l2):
            p,q=l1,l2
            dummy=ListNode()
            cur=dummy
            while p is not None and q is not None:
                if p.val<q.val:
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
            return dummy.next
        while len(lists)>1:
            merged=[]
            for i in range(0,len(lists)-1,2):
                node=merge_two(lists[i],lists[i+1])
                merged.append(node)
            if len(lists)%2!=0:
                merged.append(lists[-1])
            lists=merged
        return lists[0]



        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        