class ProductManager:
    def __init__(self):
        self.products = []
        
    def dodaj_proizvod(self, proizvod):
        self.products.append(proizvod)
        
    def ukupna_vrednost(self):
        ukupno = 0

        for product in self.products:
            ukupno += product.price * product.quantity
        return ukupno
    def prikazi_sve_proizvode(self):
        for product in self.products:
            product.prikazi_informacije()