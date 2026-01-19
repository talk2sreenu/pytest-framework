import pdb
numbers = range(20)

even_numbers = [(n, 'Even') if n % 2 == 0 else (n, 'Odd') for n in numbers]
print(even_numbers)

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long(word):
    print(word)
    return len(word) > 4

long_worlds = list(filter(is_long, words))
print(long_worlds)

another_try = [word for word in words if len(word) > 4]
another_try.sort()
print(another_try)

pizza = {
    'name' : 'Pepperoni',
    'size' : 'Large',
    'price': 19.99,
    'toppings': ['Pepperoni', 'Mushrooms', 'Onions']
}

print(pizza.keys())
print(pizza.values())
print(pizza.items())

print(pizza.pop('size', 10))
print(pizza)
print(pizza.pop('size', 10))

products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}
discounted_products = {name: price * 0.9 for name, price in products.items() if price > 100}
print(discounted_products)

for price in products.values():
    print(price)

for product, price in products.items():
    print(f'Product: {product}, Price: {price}')

for index, product in enumerate(products.items()):
    print(index, product)

myset = {1,2, 3}
myset.add(2)
print(myset)