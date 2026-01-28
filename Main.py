class Queue:
    def __init__(self, max):
        self.max = max
        self.data = []
    def is_empty(self):
        return len(self.data) == 0
    def is_full(self):
        return len(self.data) >= self.max
    def enqueue(self, element):
        if self.is_full():
            print("fronta je plna, neda sa pridat prvok")
            return False
        self.data.append(element)
        print("pridane: ", element)
        return True


q = Queue(30)
add = Queue(1)
print(add.enqueue(20))
print(add.enqueue(50))
print(q.is_empty())
print(q.is_full())
