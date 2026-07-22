# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # listA = []
        # listB = []

        # dummy = headA
        # while dummy:
        #     listA.append(dummy)
        #     dummy = dummy.next

        # dummy = headB
        # while dummy:
        #     listB.append(dummy)
        #     dummy = dummy.next

        # for nodeA in listA:
        #     for nodeB in listB:
        #         if nodeA == nodeB:
        #             return nodeA

        # return None

        setA = set()

        while headA:
            setA.add(headA)
            headA = headA.next

        while headB:
            if headB in setA:
                return headB
            headB = headB.next

        return None
        
        

        