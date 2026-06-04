import islamic
import islamic_to_jdn
def from_jdn(jdn: int):
    year = (30 * (jdn - 1948440) + 29) // 10631
    month = min(((jdn - islamic_to_jdn.to_jdn(year, 1, 1)) * 2 + 29) // 59 + 1, 12)
    day = jdn -islamic_to_jdn.to_jdn(year, month, 1) + 1
    return (year, month, day)     
