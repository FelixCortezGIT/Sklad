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
            print("sklad je plny, nie je miesto na dalsi tovar")
            return False
        self.data.append(element)
        print("pridane: ", element)
        return True
    def dequeue(self):
        if self.is_empty():
            print("sklad je prazdny, nie je co vyskladnit")
            return None
        removed = self.data.pop(0)
        print("vyskladnene: ", removed)
        return removed
    def show(self):
        print("na sklade: ", self.data)


def wait_enter():
    input("\npokracujte stlacenim enter...")

def menu():
    max_queue=int(input("zadaj maximalnu velkost skladu: "))
    q = Queue(max_queue)
    while True:
        print("\n1) je sklad prazdny?")
        print("2) je sklad plny?")
        print("3) pridat tovar")
        print("4) vyskladnit tovar")
        print("5) zobrazit stav skladu")
        print("0) koniec")
        choice = input("zadaj volbu: ")
        if choice == "1":
            print("ano, je prazdny" if q.is_empty() else "nie, nie je pazdny")
            wait_enter()
        elif choice == "2":
            print("ano, je plny" if q.is_full() else "nie, nie je plny")
            wait_enter()
        elif choice == "3":
            symbol = input("zadaj kod noveho tovaru na pridanie do skladu: ").strip()
            if len(symbol) == 0:
                print("nebol zadany ziaden kod")
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
