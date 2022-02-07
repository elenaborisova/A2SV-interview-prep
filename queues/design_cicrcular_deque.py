class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = []
        self.max_size = k

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.deque.insert(0, value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.deque.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.deque.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.deque.pop()
            return True
        return False

    def getFront(self) -> int:
        return self.deque[0] if self.deque else -1

    def getRear(self) -> int:
        return self.deque[-1] if self.deque else -1

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return len(self.deque) == self.max_size


# Your MyCircularDeque object will be instantiated and called as such:
myCircularDeque = MyCircularDeque(3)
print(myCircularDeque.insertLast(1))
print(myCircularDeque.insertLast(2))
print(myCircularDeque.insertFront(3))
print(myCircularDeque.insertFront(4))
print(myCircularDeque.getRear())
print(myCircularDeque.isFull())
print(myCircularDeque.deleteLast())
myCircularDeque.insertFront(4)   # return True
print(myCircularDeque.getFront())
