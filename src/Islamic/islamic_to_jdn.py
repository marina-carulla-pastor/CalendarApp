import islamic
def to_jdn(year: int,month: int,day: int) -> int:
    return (day+ (month - 1) * 29 + month // 2+ (year - 1) * 354 +(11 * year + 3) // 30 + 1948439)
