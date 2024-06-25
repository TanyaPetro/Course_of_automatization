from smartphone import Smartphone


phone1 = Smartphone("Motorola", "Razr", "+79991114455")
phone2 = Smartphone("Nokia", "Lumia", "+79842223366")
phone3 = Smartphone("Sony", "Xperia", "+79634442233")
phone4 = Smartphone("Samsung", "s23 ultra", "+79117778899")
phone5 = Smartphone("Apple", "15", "+79141234567")

catalog = [phone1, phone2, phone3, phone4, phone5]

for phones in catalog:
    print(phones.total_info())