class Queue:
    def __init__(self, max):
        self.max = max
    def is_empty(self):
        return len(self.data) == 0
    def is_full(self):
        return len(self.data) >= max()

print(Queue(50).is_empty)
print(Queue.is_full)
