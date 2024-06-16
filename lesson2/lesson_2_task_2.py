year = int(input("Какой год?"))


def is_year_leap(year):
    result = year % 4 == 0
    print('год', year, ':', result)


is_year_leap(year)
