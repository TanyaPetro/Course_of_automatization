class Address:
    index = "427310"
    town = "Вавож"
    street = "Центральная"
    home = "2"
    kvartira = "1"
   
    def __init__(self, index, town, street, home, flat):
        self.i = index
        self.t = town
        self.s = street
        self.h = home
        self.kv = flat
        
    def str_address(self):
        return ", ".join((self.i, self.t, self.s, self.h, self.kv))