from math import gcd
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        current_head = head
        while current_head and current_head.next:
            num = gcd(current_head.val, current_head.next.val)
            new_node = ListNode(num)
            new_node.next = current_head.next  # Insert the new node
            current_head.next = new_node  # Link the current node to the new node

            current_head = current_head.next.next  # Move two steps forward
        return head
