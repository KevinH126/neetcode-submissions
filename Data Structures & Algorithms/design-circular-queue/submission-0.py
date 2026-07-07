class MyCircularQueue:

    def __init__(self, k: int):
        self.front = 0
        self.rear = 0
        self.queue = [-1]*k

    def enQueue(self, value: int) -> bool:
        if self.queue[self.rear] != -1:
            return False
        self.queue[self.rear] = value
        self.rear+=1
        if self.rear == len(self.queue):
            self.rear = 0
        return True

    def deQueue(self) -> bool:
        if self.queue[self.front] == -1:
            return False
        self.queue[self.front] = -1
        self.front += 1
        if self.front == len(self.queue):
            self.front = 0
        return True


    def Front(self) -> int:
        return self.queue[self.front]

    def Rear(self) -> int:
        return self.queue[self.rear-1]

    def isEmpty(self) -> bool:
        if self.queue[self.front] == -1:
            return True
        return False

    def isFull(self) -> bool:
        if self.rear == self.front and self.queue[self.rear] != -1:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()