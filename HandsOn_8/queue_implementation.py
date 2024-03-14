class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [0] * max_size
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def enqueue(self, value):
        if self.is_full():
            raise Exception("Queue is full")
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]

def queue_main():
    queue = Queue(5)

    print("Enqueuing elements into the queue:")
    for i in range(1, 6):
        queue.enqueue(i)
        print("Front of the queue after enqueue:", queue.peek())

    print("\nDequeuing elements from the queue:")
    for _ in range(2):
        print("Dequeued element:", queue.dequeue())
        print("Front of the queue after dequeue:", queue.peek())

if __name__ == "__main__":
    queue_main()
