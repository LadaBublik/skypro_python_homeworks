year = int(input())


def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


x = is_year_leap(year)  # function result
print('Год', year, ':', x)
