# Topics
- Linked List
- Hash Table
- Python3

# Intuition
- The goal is to modify a linked list by removing all nodes whose values appear in a given list nums.
- This involves traversing the linked list and selectively removing nodes.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- Convert the list `nums` to a set for `O(1)` lookup times.
- Use a pointer `temp_head` to traverse the linked list.
- Use another pointer `previous` to keep track of the previous node.
- If `temp_head.val` is in `nums`, adjust the next pointers to skip the current node.
- Continue traversing the list until the end is reached.
- Return the modified head of the linked list.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)`, where `n` is the number of nodes in the linked list. We traverse the list once and perform `O(1)` operations at each node.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(m)`, where `m` is the size of nums since we are storing it in a set.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
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

```