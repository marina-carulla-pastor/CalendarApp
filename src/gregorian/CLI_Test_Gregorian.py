import gregorian
import gregorian_jdn


to_from = int(input("1. To JDN\n2. From JDN\n"))


if to_from == 1:
    year = int(input("Year: "))
    month = int(input("Month: "))
    day = int(input("Day: "))

    jdn = gregorian_jdn.to_jdn(year, month, day)
    print("JDN:", jdn)

else:
    jdn = int(input("JDN: "))

    date = gregorian_jdn.from_jdn(jdn)
    print("Gregorian:", date)
