# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        previous_node = None
        current_node = head
        next_node = current_node.next

        while current_node != None:
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node
                next_node = current_node.next if current_node else None

        return previous_node



