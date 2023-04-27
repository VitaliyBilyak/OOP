class Shop():
    def __init__(self, shop_name,store_type):
        self.shop_name=shop_name
        self.store_type=store_type
        self.number_of_units=0
    def describe_shop(self):
        print(f"Назва магазину- {self.shop_name}")
        print(f"Тип магазину- {self.store_type}")
    def open_shop(self):
        print( f"{self.shop_name} відкритий")
    def set_number_of_units(self,num):
        self.number_of_units=num
    def increment_number_of_units(self,num):
        self.number_of_units+=num

shop=Shop('Mars','clothes')
shop2=Shop('Nike','shoes')
shop3=Shop('Adidas','clothes and shoes')

print('Завдання a')
shop.open_shop()
shop.describe_shop()

print('Завдання b')
shop.describe_shop()
shop2.describe_shop()
shop3.describe_shop()

print('Завдання c')
store=Shop('Niva','food')
print(store.number_of_units)
store.number_of_units=5
print(store.number_of_units)

print('Завдання d')
print(store.number_of_units)
shop.set_number_of_units(5)
print(shop.number_of_units)
shop.increment_number_of_units(10)
print(shop.number_of_units)

print('Завдання e')
class Discount(Shop):
    def __init__(self, shop_name,store_type,discount_products):
        super().__init__(shop_name,store_type)
        self.discount_products=discount_products
    def get_discounts_ptoducts(self):
        print(f'Продукти зі знишкою: {self.discount_products}')
    def describe_shop(self):
        super().describe_shop()
        print(f'Продукти зі знишкою: {self.discount_products}')

store_discount=Discount('ava','food','milk,apple,bread')
store_discount.get_discounts_ptoducts()


