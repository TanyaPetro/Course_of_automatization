from address import Address
from mailing import Mailing


to_address = Address("123456", "Г. Ижевск", "ул. Холмогорова", "52", "20")
from_address = Address("654321", "Г. Волгоград", "ул. Космонавтов", "13", "5")


sending = Mailing(to_address, from_address, 1674, "9876456342")

print("Отправление",sending.t,"из",sending.fr.str_address(),"в",sending.to.str_address(),". Стоимость",sending.c,"рублей.")