from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        length = 0
        current_head = head
        while current_head:
            length += 1
            current_head = current_head.next

        part_size = length // k

        larger_parts = length % k
        result = []
        current_head = head

        for i in range(k):
            part_head = current_head  # Start of the current part
            part_length = part_size + (
                1 if i < larger_parts else 0
            )  # Size of this part

            # Move the pointer to the end of this part
            for _ in range(part_length - 1):
                if current_head:
                    current_head = current_head.next

            # Break the link to the next part
            if current_head:
                next_part = current_head.next
                current_head.next = None  # End the current part
                current_head = next_part  # Move to the next part

            result.append(part_head)  # Add this part to the result list

        return result
