# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        node1 = 0
        node2 = 0

        sumNode = ListNode()
        sumPointer = sumNode

        if l1 is not None:
            node1 = l1
        if l2 is not None:
            node2 = l2

        while counter or node1 or node2:
            total = 0

            if node1:
                total += node1.val
                node1 = node1.next
            if node2:
                total += node2.val
                node2 = node2.next
            
            total += counter;
            counter = total // 10

            sumPointer.val = total % 10

            if node1 or node2 or counter:
                sumPointer.next = ListNode()
                sumPointer = sumPointer.next

        return sumNode;
            

            



