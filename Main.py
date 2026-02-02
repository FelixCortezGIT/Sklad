class Goods:
    def __init__(self, code: str, quantity: int, name: str, year: int, manufacturer: str, price: float):
        self.code = code
        self.quantity = quantity
        self.name = name
        self.year = year
        self.manufacturer = manufacturer
        self.price = price
    def __repr__(self):
        return f"goods (code={self.code}, qty={self.quantity}, name={self.name}, year={self.year}, manufacturer={self.manufacturer}, price=£{self.price})"

class Palletplaces:
    def __init__(self, location_id: str):
        self.location = location_id
        self.goods = {}
    def add_goods(self, goods_code, qty):
        if qty <= 0:
            print("mnozstvo musi byt vecsie ako 0")
            return None
        self.goods[goods_code] = self.goods.get(goods_code, 0) + qty
        return self.goods[goods_code]
    def remove_goods(self, goods_code, qty):
        if qty <= 0:
            print("mnozstvo musi byt vecsie ako 0")
            return None
        if goods_code not in self.goods:
            print(f"tovar {goods_code} sa na mieste nenachadza")
            return None
        if self.goods[goods_code] < qty:
            print(f"nedostatok tovaru. dostupne: {self.goods[goods_code]}")
            return None
        self.goods[goods_code] -= qty
        remaining = self.goods[goods_code]
        if remaining == 0:
            del self.goods[goods_code]
        return remaining
    def is_empty(self):
        return len(self.goods) == 0
    def list_all(self):
        return dict(self.goods)
    def get_quantity(self):
        return sum(self.goods.values())
    def __repr__(self):
        return f"palet places: (location={self.location}, goods={self.goods})"

class Warehouse:
    def __init__(self, location: str = ""):
        self.location = location
        self.places = {}
        self.goods_catalog = {}
    def add_place(self, location_id):
        if location_id in self.places:
            print(f"miesto {location_id} uz existuje")
            return False
        self.places[location_id] = Palletplaces(location_id)
        print(f"miesto {location_id} bolo pridane")
        return True
    def remove_place(self, location_id):
        if location_id not in self.places:
            print(f"miesto {location_id} neexistuje")
            return False
        if not self.places[location_id].is_empty():
            print(f"miesto {location_id} nie je prazdne")
            return False
        del self.places[location_id]
        print(f"miesto {location_id} zmazane")
        return True
    def list_place(self, location_id):
        if location_id not in self.places:
            print(f"miesto {location_id} neexistuje")
            return
        place = self.get_place(location_id)
        print(f"miesto: {place.location}")
        goods_list = place.list_all()
        if goods_list:
            print(f"tovar na mieste: {location_id}")
            for code, qty in goods_list.items():
                if code not in self.goods_catalog:
                    print(f"tovar {code} - {qty}ks nie je v katalogu")
                    continue
                goods_info = self.get_goods(code)
                print(f"tovar: {code}: {goods_info.name} - {qty} ks (cena: {goods_info.price}€/ks)")
            print(f"\ncelkovy pocet kusov: {place.get_quantity()}")
        else:
            print("miesto je prazdne")
    def find_material(self, code):
        if code not in self.goods_catalog:
            print(f"tovar {code} neexistuje v katalogu")
            return
        goods = self.get_goods(code)
        print(f"najdeny tovar:")
        print(goods)
        print(f"\ntovar sa nachadza na miestach:")
        found = False
        for location_id, place in self.places.items():
            if code in place.goods:
                print(f"  • {location_id}: {place.goods[code]} ks")
                found = True
        if not found:
            print("tovar sa nenachadza na ziadnom mieste v sklade")
    def move_to_place(self, location_id, goods_code):
        try:
            qty = int(input("zadaj mnozstvo: "))
        except ValueError:
            print("mnozstvo musi byt cislo")
            return
        if goods_code not in self.goods_catalog:
            print(f"tovar {goods_code} neexistuje")
            return
        if location_id not in self.places:
            print(f"miesto {location_id} neexistuje")
            return
        result = self.places[location_id].add_goods(goods_code, qty)
        if result is not None:
            print(f"tovar {goods_code} ({qty}ks) bol prijaty na miesto {location_id}")
        else:
            print("mnozstvo mus byt vecsie ako 0")
            pass
    def issue_from_place(self, location_id, goods_code):
        try:
            qty = int(input("zadaj mnozstvo: "))
        except ValueError:
            print("mnozstvo musi byt cislo")
            return
        if goods_code not in self.goods_catalog:
            print(f"tovar {goods_code} neexistuje v katalogu")
            return
        if location_id not in self.places:
            print(f"miesto {location_id} neexistuje")
            return
        result = self.places[location_id].remove_goods(goods_code, qty)
        if result is not None:
            print(f"tovar {goods_code} ({qty}ks) bol vydany z miesta {location_id}")
    def change_place(self, from_loc, to_loc, goods_code):
        try:
            qty = int(input("zadaj mnozstvo: "))
        except ValueError:
            print("mnozstvo musi byt cislo")
            return
        if goods_code not in self.goods_catalog:
            print(f"tovar {goods_code} neexistuje v katalogu")
            return
        if from_loc not in self.places:
            print(f"miesto {from_loc} neexistuje")
            return
        if to_loc not in self.places:
            print(f"miesto {to_loc} neexistuje")
            return
        remaining = self.places[from_loc].remove_goods(goods_code, qty)
        if remaining is None:
            return None
        self.places[to_loc].add_goods(goods_code, qty)
        print(f"tovar {goods_code} ({qty} ks) bol premiestneny z {from_loc} na {to_loc}")
    def show_catalog(self):
        print("katalog tovaru")
        if self.goods_catalog:
            for code, goods in self.goods_catalog.items():
                print(f"\nkod: {code}")
                print(f"  nazov: {goods.name}")
                print(f"  vyrobca: {goods.manufacturer}")
                print(f"  rok vyroby: {goods.year}")
                print(f"  cena: {goods.price}€")
            print(f"celkovy pocet poloziek v katalogu: {len(self.goods_catalog)}")
        else:
            print("katalog je prazdny")
    def get_goods(self, code):
        if code not in self.goods_catalog:
            print(f"tovar {code} neexistuje")
        return self.goods_catalog[code]
    def get_place(self, location_id):
        if location_id not in self.places:
            print(f"miesto {location_id} neexistuje")
        return self.places[location_id]
    def show(self):
        if not self.places:
            print("\nsklad je zatial bez paletovych miest")
        else:
            print("\nstav paletovych miest v sklade:")
            for place in self.places.values():
                print(place)
    def __repr__(self):
        return f"warehouse (location={self.location}, places={len(self.places)}, goods={len(self.goods_catalog)})"



def wait_enter():
    input("\npokracuj stlacenim enter...")

def menu():
    w = Warehouse()
    tovar1 = Goods("T001", 100, "Notebook", 2024, "Dell", 899.99)
    tovar2 = Goods("T002", 50, "Monitor", 2023, "Samsung", 299.50)
    tovar3 = Goods("T003", 150, "Myš", 2024, "Logitech", 25.00)
    w.goods_catalog[tovar1.code] = tovar1
    w.goods_catalog[tovar2.code] = tovar2
    w.goods_catalog[tovar3.code] = tovar3
    while True:
        print("\n1) pridat paletove miesto")
        print("2) zmazat paletove miesto")
        print("3) vypis tovar na paletovom mieste")
        print("4) najdi tovar podla kodu")
        print("5) prijat tovar na paletove miesto")
        print("6) vydat tovar z paletoveho miesta")
        print("7) premiestnit tovar z miesta na miesto v sklade")
        print("8) zobrazit stav skladu")
        print("9) zobrazit katalog tovaru")
        print("0) koniec")
        choice = input("zadaj volbu: ").strip()
        if choice == "1":
            location_id = input("\nzadaj nazov noveho miesta v sklade: ").strip()
            w.add_place(location_id)
            wait_enter()
        elif choice == "2":
            location_id = input("\nzadaj nazov miesta na zmazanie: ").strip()
            w.remove_place(location_id)
            wait_enter()
        elif choice == "3":
            location_id = input("\nzadaj miesto ktore si chces pozriet: ").strip()
            w.list_place(location_id)
            wait_enter()
        elif choice == "4":
            code = input("\nzadaj kod materialu na vyhladavanie: ").strip()
            w.find_material(code)
            wait_enter()
        elif choice == "5":
            location_id = input("\nzadaj nazov miesta: ").strip()
            code = input("zadaj kod tovaru na zaskladnenie: ").strip()
            w.move_to_place(location_id, code)
            wait_enter()
        elif choice == "6":
            location_id = input("\nzadaj nazov miesta: ").strip()
            code = input("zadaj kod tovaru na vydanie: ").strip()
            w.issue_from_place(location_id, code)
            wait_enter()
        elif choice == "7":
            from_loc = input("\nzadaj z ktoreho miesta chces premiestnit tovar: ").strip()
            to_loc = input("zadaj nove miesto pre tovar: ").strip()
            code = input("zadaj kod tovaru: ").strip()
            w.change_place(from_loc, to_loc, code)
            wait_enter()
        elif choice == "8":
            w.show()
            wait_enter()
        elif choice == "9":
            w.show_catalog()
            wait_enter()
        elif choice == "0":
            print("\nkoniec")
            break
        else:
            print("neplatna volba")
            wait_enter()

menu()
