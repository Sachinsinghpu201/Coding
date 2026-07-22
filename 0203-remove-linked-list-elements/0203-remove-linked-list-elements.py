# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0,head)
        prev = dummy
        ptr = head
        while ptr:
            if ptr.val == val:
                prev.next = ptr.next
            else:
                prev = ptr
            ptr = ptr.next
        return dummy.next

        