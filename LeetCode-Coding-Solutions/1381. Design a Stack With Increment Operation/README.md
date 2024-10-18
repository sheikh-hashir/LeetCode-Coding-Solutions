# Intuition
- The problem involves building a custom stack that has a fixed size limit and supports operations to increment the bottom `k` elements.
- By using a list to represent the stack, we can efficiently perform `push`, `pop`, and `increment` operations, while keeping track of the current size to ensure we respect the stack's size limit.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Push Operation:**
  - Adds an element to the stack if it isn't full. We use a simple check on the current size before appending the element.
- **Pop Operation:**
  - Removes and returns the top element of the stack if it isn't empty. If the stack is empty, return `-1`.
- **Increment Operation:**
  - Increments the first `k` elements by a given value. If `k` is larger than the stack size, we only increment the elements that exist.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
  - **push:** `O(1)`, as appending to the list is a constant-time operation.
  - **pop:** `O(1)`, as removing the last element is constant-time.
  - **increment:** `O(k)`, where k is the number of elements to increment. If `k` is larger than the current size, it's `O(n)`, where `n` is the size of the stack.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)`, where `n` is the maximum stack size. We need space to store the elements in the list.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class CustomStack:
    def __init__(self, maxSize: int):
        self.size = maxSize
        self.current_size = 0
        self.arr = []

    def is_full(self) -> bool:
        return self.size == self.current_size

    def push(self, x: int) -> None:
        if not self.is_full():
            self.arr.append(x)
            self.current_size += 1

    def pop(self) -> int:
        if self.current_size != 0:
            self.current_size -= 1
            return self.arr.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.arr))):
            self.arr[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

```