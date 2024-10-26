# Intuition
- The problem involves creating a deque (double-ended queue) that allows insertion and deletion at both ends, along with additional operations like checking if the deque is empty or full.
- This data structure has to support a fixed maximum size and should allow efficient operations on both ends.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- We can implement the deque using a list (`arr`) with a size limit (`k`). Each operation, like insertion at the front or the rear, can be handled by manipulating the list. Additional helper functions `incrementSize` and `decrementSize` manage the current size of the deque, while the `isFull` and `isEmpty` methods help determine if we can insert new elements or not.

- **Insertion (`insertFront`, `insertLast`):**
  - Checks if the deque is full. If not, it inserts at the respective end and updates the current size.
- **Deletion (`deleteFront`, `deleteLast`):**
  - Removes the element from the respective end and updates the current size.
- **Access (`getFront`, `getRear`):**
  - Retrieves the element from the respective end.
- **Capacity checks (`isEmpty`, `isFull`):**
  - Determine if the deque is empty or full based on its current size.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
  - Insertions and deletions at the front involve shifting elements: `O(n)`.
  - Insertions and deletions at the rear are constant time: `O(1)`.
  - Checking if full/empty and getting front/rear elements are constant time: `O(1)`.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
  - We are maintaining a list of size k: `O(k)`.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.current_size = 0
        self.arr = []

    def incrementSize(self):
        self.current_size += 1

    def decrementSize(self):
        self.current_size -= 1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr.insert(0, value)
        self.incrementSize()
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr.append(value)
        self.incrementSize()
        return True

    def deleteFront(self) -> bool:
        if not self.arr:
            return False
        self.arr.pop(0)
        self.decrementSize()
        return True

    def deleteLast(self) -> bool:
        if not self.arr:
            return False
        self.arr.pop()
        self.decrementSize()
        return True

    def getFront(self) -> int:
        return self.arr[0] if self.arr else -1

    def getRear(self) -> int:
        return self.arr[-1] if self.arr else -1

    def isEmpty(self) -> bool:
        return self.current_size == 0

    def isFull(self) -> bool:
        return self.size == self.current_size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
```