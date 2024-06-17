month = input("Введите номер месяца от 1 до 12:")
month_as_number = int(month)


def month_to_season(month_as_number):
    if month_as_number in [1, 2, 12]:
        print("Зима")
    elif month_as_number in [3, 4, 5]:
        print("Весна")
    elif month_as_number in [6, 7, 8]:
        print("Лето")
    elif month_as_number in [9, 10, 11]:
        print("Осень")
    else:
        print("Некорректный ввод, нужно ввести число от 1 до 12")


month_to_season(month_as_number)
