# Topics
- Linked List
- Python3

# Intuition
- The task is to split a singly linked list into `k` parts.
- If the linked list cannot be evenly divided, the first few parts should be larger by one node.
- This problem can be approached by determining the total length of the linked list and then calculating the size of each part accordingly.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Calculate the Total Length:**
  - Traverse the linked list to find its total length.
- **Determine the Size of Each Part:**
  - Each part should have a base size of `length // k`.
  - The first `length % k` parts will have one extra node to handle the remainder.
- **Split the List:**
  - Traverse the linked list again, splitting it into parts of the calculated sizes.
  - For each part, break the link to the next node and store the head of the part in the result list.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)`, where `n` is the total number of nodes in the linked list. This is because we traverse the list twice: once to calculate the length and once to split it.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(k)` for the result list, where `k` is the number of parts.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
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
            part_length = part_size + (1 if i < larger_parts else 0)  # Size of this part

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

```
