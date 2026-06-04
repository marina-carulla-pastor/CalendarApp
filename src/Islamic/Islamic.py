from dataclasses import dataclass

@dataclass
class IslamicDate:
    year: int
    month: int
    day: int

MONTH_LENGTHS = [30, 29,30,29,30,29,30,29,30,29,30,29]

def is_leap_year(year: int) -> bool:
    return((11 * year + 14) % 30 < 11)

def days_in_month(year: int,month: int) -> int:
    if month == 12 and is_leap_year(year):
        return 30
    return MONTH_LENGTHS[month -1]
    
def is_valid_date(year: int,month: int,day: int) -> bool:
    if year <= 0:
        return False
    if month < 1 or month > 12:
        return False
    max_day = days_in_month(year,month)
    return 1 <= day <= max_day 
    
    max_day = days_in_month(year,month)   
    return 1 <= day <= max_day

def days_in_year(year: int) -> int:
    return 355 if is_leap_year(year) else 354
  
