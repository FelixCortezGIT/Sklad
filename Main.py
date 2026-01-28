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
    def show(self):
        print("obsah fronty: ", self.data)


# q = Queue(3)
# print(q.is_empty())
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# print(q.is_full())
# q.dequeue()
# q.dequeue()
# q.show()

def wait_enter():
    input("\npokracujte stlacenim enter...")

def menu():
    max_queue=int(input("zadaj maximalnu velkost fronty: "))
    q = Queue(max_queue)
    while True:
        print("\n1) Is Empty - je prazdna")
        print("2) Is Full - je plna")
        print("3) Enqueue - pridat znak")
        print("4) Dequeue - odstranit znak")
        print("5) SHow - zobrazit frontu")
        print("0) koniec")
        choice = input("zadaj volbu: ")
        if choice == "1":
            print("ano, je prazdna" if q.is_empty() else "nie, nie je pazdna")
            wait_enter()
        elif choice == "2":
            print("ano, je plna" if q.is_full() else "nie, nie je plna")
            wait_enter()
        elif choice == "3":
            symbol = input("zadaj znak na pridanie: ").strip()
            if len(symbol) == 0:
                print("nebol zadany ziaden znak")
            else:
                q.enqueue(symbol)
                wait_enter()
        elif choice == "4":
            q.dequeue()
            wait_enter()
        elif choice == "5":
            q.show()
            wait_enter()
        elif choice == "0":
            print("koniec")
            break
        else:
            print("neplatna volba, skus znova.")

menu()
