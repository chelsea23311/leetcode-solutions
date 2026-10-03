"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        hashmap={}
        q=head
        dummy=Node(0)
        cur=dummy
        if not head:
            return None
        while q is not None:
            if q not in hashmap:
                new_node=Node(q.val)
                hashmap[q]=new_node
            cur.next=hashmap[q]
            cur=cur.next
            if not q.random:
                cur.random=None
            elif q.random not in hashmap:
                new_node=Node(q.random.val)
                hashmap[q.random]=new_node
                cur.random=hashmap[q.random]
            else:
                cur.random=hashmap[q.random]
            q=q.next
        return dummy.next

            
        """
        :type head: Node
        :rtype: Node
        """
        