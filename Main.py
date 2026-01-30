class Goods:
    def __init__(self, code, name, year, manufacturer, price, quantity):
        self.code = code(str).strip()
        self.name = name(str).strip()
        self.year = year(int)
        self.manufacturer = manufacturer(str).strip()
        self.price = price(float)
        self.quantity = quantity(int)
    def __repr__(self):
        return (f"goods code: {self.code} quantity: {self.quantity} name: {self.name} year: {self.year} manufacturer: {self.manufacturer} price: {self.price}")

class Palletplaces:
    def __init__(self, location_id):
        self.location = location_id(str).strip()
    def add_goods(self, goods_code, qty):

    def remove_goods(self, goods_code, qty):

    def is_empty(self):

    def list_all(self):

    def get_quantity(self):

    def __repr__(self):

class Warehouse:
    def __init__(self, location):
        self.location = location(str).strip()

    def add_place(self, location_id):

    def remove_location(self, location_id,):

    def list_goods(self):

    def list_places(self):

    def get_goods(self, code):

    def goods_in(self, goods_code, qty):

    def goods_out(self, goods_code, qty):

    def move_location(self, goods_code, qty, from_loc, to_loc):







def wait_enter():
    input("\npokracujte stlacenim enter...")

def menu():
    w = Warehouse()
    while True:
        print("\n1) pridat paletove miesto")
        print("2) zmazat paletove miesto")
        print("3) vypis tovar na paletovom mieste")
        print("4) najdi tovar podla kodu")
        print("5) prijat tovar na paletove miesto")
        print("6) vydat tovar z paletoveho miesta")
        print("7) premiestnit tovar z miesta na miesto v sklade")
        print("8) zobrazit stav skladu")
        print("0) koniec")
        choice = input("zadaj volbu: ")
        if choice == "1":
            name = input("\nzadaj nazov noveho miesta v sklade: ").strip()
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
