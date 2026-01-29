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

class PalletPlace:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.queue = Queue(capacity)
    def free_slots(self):
        return self.capacity - len(self.queue.data)
    def show(self):
        print(f"[{self.name}] kapacita: {self.capacity}, obsadene: {len(self.queue.data)}, volne: {self.free_slots()}")
        self.queue.show()

class Warehouse:
    def __init__(self):
        self.places: list[PalletPlace] = []
    def add_place(self, name: str, capacity: int):
        if not name.strip():
            print("nazov paletoveho miesta nesmie byt prazdny")
            return False
        if capacity <= 0:
            print("kapacita paletoveho miesta musi byt kladne cele cislo")
            return False
        if self.get_place(name) is not None:
            print("paletove miesto s takym nazvom uz existuje")
            return False
        self.places.append(PalletPlace(name, capacity))
        print(f"paletove miesto {name} vytvorene s kapacitou {capacity}")
        return True
    def delete_place(self, name: str):
        place = self.get_place(name)
        if place is None:
            print("paletove miesto neexistuje")
            return False
        if not place.queue.is_empty():
            print("paletove miesto nie je prazdne, nemozem ho vymazat, presun najprv tovar inde")
            return False
        self.places = [p for p in self.places if p.name != name]
        print(f"paletove miesto {name} zmazane")
        return True
    def list_place(self, place_name: str):
        place = self.get_place(place_name)
        if place is None:
            print("paletove miesto neexistuje")
            return False
        place.show()
        return True
    def find_material(self, item_code: str):
        if not item_code.strip():
            print("kod tovaru nesmie byt prazdny")
            return []
        found = []
        for p in self.places:
            for idx, code in enumerate(p.queue.data):
                if code == item_code:
                    found.append((p.name, idx))
        if not found:
            print(f"material s kodom {item_code} sa v sklade nenasiel")
        else:
            print(f"material {item_code} najdeny na {len(found)} miestach: ")
            for place_name, idx in found:
                print(f"miesto {place_name} pozicia vo fronte: {idx}")
        return found
    def get_place(self, name: str):
        for p in self.places:
            if p.name == name:
                return p
        return None
    def move_to_place(self, place_name: str, item_code: str):
        place = self.get_place(place_name)
        if place is None:
            print("paletove miesto s tymto nazvom neexistuje")
            return False
        if not item_code.strip():
            print("kod tovaru nesmie byt prazdny")
            return False
        if place.queue.is_full():
            print(f"paletove miesto {place_name} je plne")
            return False
        return place.queue.enqueue(item_code)
    def issue_from_place(self, place_name: str):
        place = self.get_place(place_name)
        if place is None:
            print("paletove miesto s tymto nazvom neexistuje")
            return None
        return place.queue.dequeue()
    def change_place(self, source_place: str, target_place: str):
        if not source_place.strip() or not target_place.strip():
            print("nazvy paletovych miest nesmu byt prazdne")
            return False
        if source_place == target_place:
            print("miesta Z a DO sa zhoduju")
            return False
        source = self.get_place(source_place)
        target = self.get_place(target_place)
        if source is None:
            print(f"plaetove miesto {source_place} neexistuje")
            return False
        if target is None:
            print(f"paletove miesto {target_place} neexistuje")
            return False
        if source.queue.is_empty():
            print(f"z ktoreho paletove miesto {source_place} je prazdne, nie je co premiestnit")
            return False
        if target.queue.is_full():
            print(f"cielove paletove miesto {target_place} je plne, neda sa premiestnit")
            return False
        item = source.queue.dequeue()
        if item is None:
            print("nepodarilo sa odobrat tovar zo zdroja")
            return False
        enquir = target.enqueue(item)
        if not enquir:
            print("zaskladnenie do noeho miesta zlyhalo, vraciam tovar opet na zdroj")
            source.queue.enqueue(item)
            return False
        print(f"premiestnene: {item} z {source_place} do {target_place}")
        return True
    def show(self):
        if not self.places:
            print("sklad zatial bez paletovych miest")
        else:
            print("sklad stav paletovych miest:")
            for p in self.places:
                p.show()


def wait_enter():
    input("\npokracujte stlacenim enter...")

def menu():
    w = Warehouse()
    while True:
        print("\n1) pridat paletove miesto")
        print("2) zmazat paletove miesto")
        print("3) vypis tovar na paletovom mieste")
        print("4) najdi material podla kodu")
        print("5) prijat material na paletove miesto")
        print("6) vydat material z paletoveho miesta")
        print("7) premiestnit material z miesta na miesto v sklade")
        print("8) zobrazit stav skladu")
        print("0) koniec")
        choice = input("zadaj volbu: ")
        if choice == "1":
            name = input("\nzadaj nazov noveho miesta v sklade").strip()
            try:
                capacity = int(input("zadaj kapacitu noveho miesta: "))
            except ValueError:
                print("kapacita musi byt cislo")
                wait_enter()
                continue
            w.add_place(name, capacity)
            wait_enter()
        elif choice == "2":
            name = input("zadaj nazov miesta na zmazanie: ").strip()
            w.delete_place(name)
            wait_enter()
        elif choice == "3":
            name = input("zadaj miesto ktore si chces pozriet: "). strip()
            w.list_place(name)
            wait_enter()
        elif choice == "4":
           code = input("zadaj kod materialu na vyhladavanie: ").strip()
           w.find_material(code)
           wait_enter()
        elif choice == "5":
            place = input("zadaj nazov miesta: ").strip()
            code = input("zadaj kod tovaru na zaskladnenie: ").strip()
            w.move_to_place(place, code)
            wait_enter()
        elif choice == "6":
            place = input("zadaj nazov miesta: ").strip()
            w.issue_from_place(place)
            wait_enter()
        elif choice == "7":
            source = input("zadaj z ktoreho miesta chces premiestnit tovar: ").strip()
            target = input("zadaj nove miesto pre tovar: ").strip()
            w.change_place(source, target)
            wait_enter()
        elif choice == "8":
            w.show()
            wait_enter()
        elif choice == "0":
            print("koniec")
            break
        else:
            print("neplatna volba, skus znova.")

menu()
