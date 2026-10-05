from product import Product
from product_manager import ProductManager
manager = ProductManager()
laptop = Product("Laptop", 1400, 5)

manager.dodaj_proizvod(laptop)

mouse = Product("mouse", 500, 10)

manager.dodaj_proizvod(mouse)

monitor = Product("monitor", 30, 50)
manager.dodaj_proizvod(monitor)
manager.prikazi_sve_proizvode()
manager.ukupna_vrednost()
print (manager.ukupna_vrednost())