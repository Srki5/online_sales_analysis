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
manager.izbrisi_proizvod(mouse)
cart = Cart()
cart.dodaj_proizvod(laptop)
cart.dodaj_proizvod(mouse)
cart.dodaj_proizvod(monitor)
print(cart.ukupna_vrednost())
cart.prikazi_sadrzaj()