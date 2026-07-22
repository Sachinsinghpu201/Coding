# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution(object):
#     def sortList(self, head):
#         """
#         :type head: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         listA = []
#         curr = head
#         while curr:
#             listA.append([curr,curr.val])
#             curr = curr.next
#         listA.sort(key= lambda x:x[1] )    

#         dummy = ListNode(0)
#         dummy.next = None
#         tail = dummy 
#         for i in range(len(listA)):
#             dummy.next = listA[i][0]
#             dummy = dummy.next
#         dummy.next = None

#         return  tail.next

class Solution(object):

    def sortList(self, head):

        if not head or not head.next:
            return head

        # Find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # Sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge
        return self.merge(left, right)


    def merge(self, l1, l2):

        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:

            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        tail.next = l1 if l1 else l2

        return dummy.next