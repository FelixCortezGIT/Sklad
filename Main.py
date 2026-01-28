class Queue:
    def __init__(self, max):
        self.max = max
        self.data = []
    def is_empty(self):
        return len(self.data) == 0
    def is_full(self):
        return len(self.data) >= self.max

q = Queue(30)
print(q.is_empty())
print(q.is_full())
