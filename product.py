class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def prikazi_informacije(self):
            print(f"Proizvod: {self.name}")
            print(f"Cena: {self.price}")
            print(f"Kolicina: {self.quantity}")
    def azuriraj_kolicinu(self, nova_kolicina):
            self.quantity = nova_kolicina