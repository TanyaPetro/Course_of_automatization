class User:
    
    def __init__(self, first_name, last_name):
        self.name1 = first_name
        self.name2 = last_name
        
    def sayName1(self):
        print(self.name1)
        
    def sayName2(self):
        print(self.name2)
        
    def sayNames(self):
        print(self.name1, self.name2)