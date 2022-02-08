class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        mid = len(self.queue) // 2
        self.queue.insert(mid, val)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        return self.queue.pop(0) if self.queue else -1

    def popMiddle(self) -> int:
        mid = (len(self.queue) - 1) // 2
        if 0 <= mid < len(self.queue):
            return self.queue.pop(mid)
        return -1

    def popBack(self) -> int:
        return self.queue.pop() if self.queue else -1


# Test cases:
q = FrontMiddleBackQueue()
print(q.pushFront(1))     # [1]
print(q.pushBack(2))      # [1, 2]
print(q.pushMiddle(3))    # [1, 3, 2]
print(q.pushMiddle(4))    # [1, 4, 3, 2]
print(q.popFront())       # return 1 -> [4, 3, 2]
print(q.popMiddle())      # return 3 -> [4, 2]
print(q.popMiddle())      # return 4 -> [2]
print(q.popBack())        # return 2 -> []
print(q.popFront())       # return -1 -> [] (The queue is empty)
