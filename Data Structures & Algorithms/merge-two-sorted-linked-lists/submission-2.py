# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy_ptr = dummy

        node_one = list1
        node_two = list2

        while (node_one or node_two) and dummy_ptr:
            while node_one and node_two and dummy_ptr:
                if node_one.val <= node_two.val:
                    dummy_ptr.next = node_one
                    dummy_ptr = node_one
                    node_one = node_one.next
                else:
                    dummy_ptr.next = node_two
                    dummy_ptr = node_two
                    node_two = node_two.next
            
            dummy_ptr.next = node_one or node_two
            dummy_ptr = dummy_ptr.next
            node_one = node_one.next if node_one else None
            node_two = node_two.next if node_two else None
        
        return dummy.next

