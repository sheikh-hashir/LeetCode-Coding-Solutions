class MyCircularDeque:
    def __init__(self, k: int):
        self.size = k
        self.current_size = 0
        self.arr = []

    def incrementSize(self) -> None:
        self.current_size += 1

    def decrementSize(self) -> None:
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
