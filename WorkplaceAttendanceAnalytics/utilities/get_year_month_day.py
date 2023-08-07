def is_leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        return False
    elif year % 4 == 0:
        return True
    return False


def get_year_month_day(date):
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[-2:])
    month_code = {1: (1, 'JAN'), 2: (4, 'FEB'), 3: (4, 'MAR'), 4: (0, 'APR'), 5: (2, 'MAY'), 6: (5, 'JUN'), 7: (0, 'JUL'), 8: (3, 'AUG'),
                  9: (6, 'SEP'), 10: (1, 'OCT'), 11: (4, 'NOV'), 12: (6, 'DEC')}
    century_code = {15: 0, 16: 6, 17: 4, 18: 2, 19: 0, 20: 6, 21: 4, 22: 2}
    day_code = {0: 'Saturday', 1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday'}

    mc = month_code[month][0]
    cc = century_code[year // 100]
    num_years_completed = year % 100
    num_of_leap_year = num_years_completed // 4

    leap_year = is_leap_year(year)

    diff = 0
    if leap_year and month in (1, 2):
        diff = 1

    val = day + mc + cc + num_years_completed + num_of_leap_year - diff

    day_of_the_week = day_code[val % 7]

    month = month_code[month][1]

    return year, month, day_of_the_week


if __name__ == "__main__":
    year, month, day = get_year_month_day('2023-08-07')

    print(year, month, day)
