from product import Product
from product_manager import ProductManager
from cart import Cart
manager = ProductManager()
laptop = Product("Laptop", 1400, 5)

manager.dodaj_proizvod(laptop)

mouse = Product("mouse", 500, 10)

manager.dodaj_proizvod(mouse)

monitor = Product("monitor", 30, 50)
manager.dodaj_proizvod(monitor)
manager.prikazi_sve_proizvode()
print (manager.ukupna_vrednost())

manager.izbrisi_proizvod(mouse)
manager.prikazi_sve_proizvode()
cart = Cart()
cart.dodaj_proizvod(laptop)
cart.dodaj_proizvod(mouse)
cart.dodaj_proizvod(monitor)
print(cart.ukupna_vrednost())
cart.prikazi_sadrzaj()