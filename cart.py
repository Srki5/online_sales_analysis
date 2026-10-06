class Cart:
    def __init__(self):
        self.cart_items = []
        
    def dodaj_proizvod(self, proizvod):
        self.cart_items.append(proizvod)
        
    def ukupna_vrednost(self):
        ukupno = 0
        
        for items in self.cart_items:
            ukupno += items.price * items.quantity
        return ukupno
    def prikazi_sadrzaj(self):
        for items in self.cart_items:
            items.prikazi_informacije()