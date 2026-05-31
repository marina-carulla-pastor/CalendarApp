from dataclasses import dataclass

@dataclass
class GregorianDate:
    year: int
    month: int
    day: int

MONTH_LENGTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year: int) -> bool:
    return (
        year % 4 == 0 and
        (year % 100 != 0 or year % 400 == 0)
    )

def days_in_month(year: int, month: int) -> int:
    if month == 2 and is_leap_year(year):
        return 29

    return MONTH_LENGTHS[month - 1]

def is_valid_date(year: int, month: int, day: int) -> bool:
    if year <= 0:
        return False

    if month < 1 or month > 12:
        return False

    max_day = days_in_month(year, month)

    return 1 <= day <= max_day
  
def days_in_year(year: int) -> int:
    return 366 if is_leap_year(year) else 365
