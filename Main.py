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
            raise ValueError("mnozstvo musi byt vecsie ako 0")
        self.goods[goods_code] = self.goods.get(goods_code, 0) + qty
        return self.goods[goods_code]
    def remove_goods(self, goods_code, qty):
        if qty <= 0:
            raise ValueError("mnozstvo musi byt vecsie ako 0")
        if goods_code not in self.goods:
            raise KeyError(f"tovar {goods_code} sa na mieste nenachadza")
        if self.goods[goods_code] < qty:
            raise ValueError(f"nedostatok tovaru. dostupne: {self.goods[goods_code]}")
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
            raise ValueError(f"miesto {location_id} uz existuje")
        self.places[location_id] = Palletplaces(location_id)
    def remove_place(self, location_id):
        if location_id not in self.places:
            raise KeyError(f"miesto {location_id} neexistuje")
        if not self.places[location_id].is_empty():
            raise ValueError(f"miesto {location_id} nie je prazdne")
        del self.places[location_id]
    def list_goods(self):
        return dict(self.goods_catalog)
    def list_places(self):
        return list(self.places.keys())
    def get_goods(self, code):
        if code not in self.goods_catalog:
            raise KeyError(f"tovar {code} neexistuje")
        return self.goods_catalog[code]
    def get_place(self, location_id):
        if location_id not in self.places:
            raise KeyError(f"miesto {location_id} neexistuje")
        return self.places[location_id]
    def goods_in(self, goods_code, qty, location_id):
        if goods_code not in self.goods_catalog:
            raise KeyError(f"tovar {goods_code} neexistuje")
        if location_id not in self.places:
            raise KeyError(f"miesto {location_id} neexistuje")
        self.places[location_id].add_goods(goods_code, qty)
        return self.places[location_id]
    def goods_out(self, goods_code, qty, location_id):
        if goods_code not in self.goods_catalog:
            raise KeyError(f"tovar {goods_code} neexistuje")
        if location_id not in self.places:
            raise KeyError(f"miesto {location_id} neexistuje")
        self.places[location_id].remove_goods(goods_code, qty)
        return self.places[location_id]
    def move_location(self, goods_code, qty, from_loc, to_loc):
        if goods_code not in self.goods_catalog:
            raise KeyError(f"tovar {goods_code} neexistuje")
        if from_loc not in self.places:
            raise KeyError(f"miesto {from_loc} neexistuje")
        if to_loc not in self.places:
            raise KeyError(f"miesto {to_loc} neexistuje")
        self.places[from_loc].remove_goods(goods_code, qty)
        self.places[to_loc].add_goods(goods_code, qty)
        return from_loc, to_loc
    def show(self):
        if not self.places:
            print("sklad zatial bez paletovych miest")
        else:
            print("sklad stav paletovych miest:")
            for place in self.places.values():
                print(place)
    def __repr__(self):
        return f"warehouse (location={self.location}, places={len(self.places)}, goods={len(self.goods_catalog)})"



def menu():
    w = Warehouse()
    print("\npridanie paletovych miest: ")
    w.add_place("A100")
    w.add_place("A200")
    w.add_place("B100")
    print(f"sklad opbsahuje miesta: {w.list_places()}")
    tovar1 = Goods("T001", 100, "Notebook", 2024, "Dell", 899.99)
    tovar2 = Goods("T002", 50, "Monitor", 2023, "Samsung", 299.50)
    tovar3 = Goods("T003", 150, "Myš", 2024, "Logitech", 25.00)
    print("\ntovar:")
    print(tovar1)
    print(tovar2)
    print(tovar3)
    print("\npridanie tovaru:")
    w.goods_catalog[tovar1.code] = tovar1
    w.goods_catalog[tovar2.code] = tovar2
    w.goods_catalog[tovar3.code] = tovar3
    print(w.show())
    w.goods_in("T001", 10, "A100")
    w.goods_in("T002", 5, "A100")
    w.goods_in("T003", 7, "A200")
    w.goods_in("T001", 15, "B100")
    print()
    print(w.show())
    print(f"\nzoznam tovaru na mieste {w.get_place('A100').location}")
    print(w.get_place("A100").list_all())
    print("\nvydaj tovaru:")
    w.goods_out("T001", 3, "A100")
    print(w.get_place("A100"))
    print("\npresun tovaru:")
    from_loc, to_loc = w.move_location("T001", 3, "B100", "A200")
    print(f"miesto {from_loc}: {w.get_place(from_loc)}")
    print(f"miesto {to_loc}: {w.get_place(to_loc)}")
menu()

# def wait_enter():
#     input("\npokracujte stlacenim enter...")

# def menu():
#     w = Warehouse()
#     while True:
#         print("\n1) pridat paletove miesto")
#         print("2) zmazat paletove miesto")
#         print("3) vypis tovar na paletovom mieste")
#         print("4) najdi tovar podla kodu")
#         print("5) prijat tovar na paletove miesto")
#         print("6) vydat tovar z paletoveho miesta")
#         print("7) premiestnit tovar z miesta na miesto v sklade")
#         print("8) zobrazit stav skladu")
#         print("0) koniec")
#         choice = input("zadaj volbu: ")
#         if choice == "1":
#             name = input("\nzadaj nazov noveho miesta v sklade: ").strip()
#             try:
#                 capacity = int(input("zadaj kapacitu noveho miesta: "))
#             except ValueError:
#                 print("kapacita musi byt cislo")
#                 wait_enter()
#                 continue
#             w.add_place(name, capacity)
#             wait_enter()
#         elif choice == "2":
#             name = input("zadaj nazov miesta na zmazanie: ").strip()
#             w.delete_place(name)
#             wait_enter()
#         elif choice == "3":
#             name = input("zadaj miesto ktore si chces pozriet: "). strip()
#             w.list_place(name)
#             wait_enter()
#         elif choice == "4":
#            code = input("zadaj kod materialu na vyhladavanie: ").strip()
#            w.find_material(code)
#            wait_enter()
#         elif choice == "5":
#             place = input("zadaj nazov miesta: ").strip()
#             code = input("zadaj kod tovaru na zaskladnenie: ").strip()
#             w.move_to_place(place, code)
#             wait_enter()
#         elif choice == "6":
#             place = input("zadaj nazov miesta: ").strip()
#             w.issue_from_place(place)
#             wait_enter()
#         elif choice == "7":
#             source = input("zadaj z ktoreho miesta chces premiestnit tovar: ").strip()
#             target = input("zadaj nove miesto pre tovar: ").strip()
#             w.change_place(source, target)
#             wait_enter()
#         elif choice == "8":
#             w.show()
#             wait_enter()
#         elif choice == "0":
#             print("koniec")
#             break
#         else:
#             print("neplatna volba, skus znova.")
#
# menu()
