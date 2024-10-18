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
