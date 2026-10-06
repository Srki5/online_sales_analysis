import random
from product import Product
from product_manager import ProductManager
from cart import Cart
manager = ProductManager()
laptop = Product("Gaming Laptop", 1400, 7)

manager.dodaj_proizvod(laptop)

mouse = Product("mouse", 500, 10)

manager.dodaj_proizvod(mouse)

monitor = Product("monitor", 30, 50)
manager.dodaj_proizvod(monitor)

cart = Cart()
odabrani_proizvodi = random.sample(manager.products, 3)
for proizvod in odabrani_proizvodi:
   cart.dodaj_proizvod(proizvod)
cart.prikazi_sadrzaj()
print(cart.ukupna_vrednost())