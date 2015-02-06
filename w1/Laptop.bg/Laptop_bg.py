class Product():
    def __init__(self, name, firm_cost, price):
        self. name = name
        self.firm_cost = firm_cost
        self.price = price

    def profit(self):
        return self.price - self.firm_cost

class Laptop(Product):

    def __init__(self, name, firm_cost, price, hdd, ram):
        super().__init__(name, firm_cost, price)
        self.hdd = hdd
        self.ram =  ram


class Smartphone(Product):

    def __init__(self, name, firm_cost, price, display_size, mega_pixels):
        super().__init__(name, firm_cost, price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels

class Store():

    def __init__(self, name):
        self.name = name
        self.products = {}
        self.income = 0

    def load_new_products(self, item, amount):
        self.products[item] = amount

    def list_products(self, show_type):
        show_item = []
        for item in self.products.items():
            if isinstance(item[0], show_type):
                show_item.append(item)


        output_str = ""
        for i in show_item:
            output_str = output_str + str(i[0].name) + " - " + str(i[1]) + "\n"

        return output_str

    def sell_product(self, item):
        if item in self.products:
            if self.products[item] > 0 :
                self.income = self.income + item.profit()
                self.products[item] -= 1
                return True

        return False

    def total_income(self):
        return self.income

if __name__ == '__main__':

    store = Store('Laptop.bg')
    smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
    store.load_new_products(smarthphone, 2)
    print(store.sell_product(smarthphone)) # True
    print(store.sell_product(smarthphone)) # True

    print(store.total_income()) # 640