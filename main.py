# First part of homework
# Task1
class Discount:
    def discount(self):
        raise NotImplementedError


class RegularDiscount(Discount):
    def discount(self):
        return 0.9


class SilverDiscount(Discount):
    def discount(self):
        return 0.85


class GoldDiscount(Discount):
    def discount(self):
        return 0.8


class Product:
    def __init__(self, title: str, price: float | int):
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price:.2f}'



class CartIterator:

    def __init__(self, products, quantities):
        self.products = products
        self.quantities = quantities
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.products):
            self.index += 1
            return self.products[self.index - 1], self.quantities[self.index - 1]
        raise StopIteration


class Cart:
    def __init__(self, discount: Discount = None):
        self.__products = []
        self.__quantities = []
        self.discount = discount

    def add_product(self, product: Product, quantity: int | float = 1):
        if isinstance(product, Product) and isinstance(quantity, int | float):
            self.__products.append(product)
            self.__quantities.append(quantity)

    def __iter__(self):
        return CartIterator(self.__products, self.__quantities)

    def total(self):
        summa = sum(product.price * quantity for product, quantity in zip(self.__products, self.__quantities))
        return summa * self.discount.discount() if self.discount else summa

    def __iadd__(self, other):
        return Cart()

    def __str__(self):
        return '\n'.join(map(lambda items: f'{items[0]} x {items[1]} = {items[0].price * items[1]} UAH',
                             zip(self.__products, self.__quantities))) + f'\nTotal: {self.total():.2f} UAH\n'


pr_1 = Product('banana', 50)
pr_2 = Product('apple', 51)
pr_3 = Product('orange', 52)

cart_1 = Cart()
cart_2 = Cart(SilverDiscount())
cart_1 += cart_2
cart_1.add_product(pr_1)
cart_1.add_product(pr_2)
cart_1.add_product(pr_3)

cart_1.add_product(pr_1, 5)
for i in cart_1:
    print('\n'.join(map(str, i)))






# Second part of homework
# Task1
def generator_mul(stop):

    num = 2
    while num < stop:
        yield num
        num *= 2


for i in generator_mul(20):
    print(i)

# Task2
def generator_range(start, stop, step):
    while 0 < start < stop:
        yield start
        start *= step


for i in generator_range(2, 10, 3):
    print(i)

# Task3
def simple_num_generator(start, stop):
    while 0 < start < stop:
        yield start
        start += 1


for i in simple_num_generator(2, 997):
    if i % 2 != 0 and i // i and i % 3 != 0:
        print(i)

# Task4
gen_list = []


def generator_range(start):
    while start < 10000:
        yield start
        start = start ** 3


for i in generator_range(2):
    gen_list.append(i)
print(gen_list)


# Task5 розбиралили на уроці


# Task6
def simple_num_generator(start_date, stop_date):
    while 0 < start_date < stop_date:
        yield start_date
        start_date += 1


for i in simple_num_generator(1.11, 30.11):
    print(f"дата: {i:.2f} 2020")
