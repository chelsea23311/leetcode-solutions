# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        deque=[]
        node=head
        while node is not None:
            deque.append(node.val)
            node=node.next
        if deque==deque[::-1]:
            return True
        else:
            return False

        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        