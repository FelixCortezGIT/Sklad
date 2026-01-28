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
    def dequeue(self):
        if self.is_empty():
            print("fronta je prazdna, nie je co odstranit")
            return None
        removed = self.data.pop(0)
        print("odstranene: ", removed)
        return removed


q = Queue(3)
print(q.is_empty())
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.is_full())
q.dequeue()
q.dequeue()
