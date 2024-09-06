from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        nums = set(nums)
        temp_head = head
        previous = None
        while temp_head:
            if temp_head.val in nums:
                if not previous:
                    head = head.next
                    temp_head = head
                else:
                    previous.next = temp_head.next
                    temp_head = previous
                continue
            previous = temp_head
            temp_head = temp_head.next
        return head
