class Smartphone:
    phone_brand = ""
    phone_model = ""
    phone_number = "+79564326789"
    
    def __init__(self, phone_brand, phone_model, phone_number):
        self.pB = phone_brand
        self.pM = phone_model
        self.pN = phone_number
        
    def total_info(self):
        return self.pB + " - " + self.pM + ". " + self.pN + "."