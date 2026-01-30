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
    def remove_goods(self, goods_code, qty):
        if qty <= 0:
            raise ValueError("mnozstvo musi byt vecsie ako 0")
        if goods_code not in self.goods:
            raise KeyError(f"tovar {goods_code} sa na mieste nenachadza")
        if self.goods[goods_code] < qty:
            raise ValueError(f"nedostatok tovaru. dostupne: {self.goods[goods_code]}")
        self.goods[goods_code] -= qty
        if self.goods[goods_code] == 0:
            del self.goods[goods_code]
    def is_empty(self):
        return len(self.goods) == 0
    def list_all(self):
        return dict(self.goods)
    def get_quantity(self):
        return sum(self.goods.values())
    def __repr__(self):
        return f"palet places: (location={self.location}, goods={self.goods})"

# class Warehouse:
#     def __init__(self, location: str):
#         self.location = location
#
#     def add_place(self, location_id):
#
#     def remove_location(self, location_id,):
#
#     def list_goods(self):
#
#     def list_places(self):
#
#     def get_goods(self, code):
#
#     def get_place(self, location_id):
#
#     def goods_in(self, goods_code, qty):
#
#     def goods_out(self, goods_code, qty):
#
#     def move_location(self, goods_code, qty, from_loc, to_loc):
#


def menu():
    miesto = Palletplaces("A100")
    miesto = Palletplaces("A200")
    tovar1 = Goods("T001", 100, "Notebook", 2024, "Dell", 899.99)
    tovar2 = Goods("T002", 50, "Monitor", 2023, "Samsung", 299.50)
    tovar3 = Goods("T003", 150, "Myš", 2024, "Logitech", 25.00)
    print("\ntovar:")
    print(tovar1)
    print(tovar2)
    print(tovar3)
    print("\npridanie tovaru:")
    miesto.add_goods("T001", 10) # osetrenie aby sa pytal na ktore miesto pridat tovar
    miesto.add_goods("T002", 5)
    miesto.add_goods("T003", 7)
    print(miesto)
    print(f"celkove mnozstvo: {miesto.get_quantity()}")
    print(f"\nzoznam tovaru na mieste {miesto.location}")
    print(miesto.list_all())
    print("\nodobratie tovaru:")
    miesto.remove_goods("T001", 5)
    print(miesto)
    print(f"celkove mnozstvo: {miesto.get_quantity()}")
    print(f"\nprazdne: {miesto.is_empty()}")
    print("\nvyprazdnenie miesta:")
    miesto.remove_goods("T001", 5) # osetrene ak odoberies viac ako mas, spadne program
    miesto.remove_goods("T002", 5)
    miesto.remove_goods("T003", 7)
    print(miesto)
    print(f"prazdne: {miesto.is_empty()}")

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
