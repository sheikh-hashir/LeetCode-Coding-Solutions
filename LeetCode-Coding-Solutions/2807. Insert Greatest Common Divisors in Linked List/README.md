# Topics
- Linked List
- Math
- Number Theory
- Python3

# Intuition
- The problem requires inserting a node between every pair of consecutive nodes in a linked list.
- The value of the new node should be the greatest common divisor (GCD) of the values of those two consecutive nodes.
- This suggests iterating through the linked list and calculating the GCD for each consecutive pair of nodes.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- Start at the head of the linked list and iterate through the list.
- For each pair of consecutive nodes:
  - Calculate the GCD of their values.
  - Insert a new node with this GCD value between the two nodes.
- Adjust the pointers properly to maintain the linked list structure.
- Continue until the end of the list.
- Finally, return the modified linked list.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)` where `n` is the number of nodes in the linked list, because we are iterating through each node once.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)` (excluding the space required for the new nodes), as we are modifying the list in place without using extra data structures.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
from math import gcd

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_head = head
        while current_head and current_head.next:
            num = gcd(current_head.val, current_head.next.val)
            new_node = ListNode(num)
            new_node.next = current_head.next  # Insert the new node
            current_head.next = new_node  # Link the current node to the new node

            current_head = current_head.next.next  # Move two steps forward
        return head

```