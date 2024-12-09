class MyCircularQueue:

    def __init__(self, k: int):
        
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enQueue(self, value: int) -> bool:
        
        if self.isFull():
            return False
        elif self.isEmpty():
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = value
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        
        if self.isEmpty():
            return False
        elif self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.k
        return True

    def Front(self) -> int:
       
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
       
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        
        return self.head == -1

    def isFull(self) -> bool:
        
        return (self.tail + 1) % self.k == self.head


