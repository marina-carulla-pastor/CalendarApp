import gregorian
import gregorian_to_jdn
import from_jdn_gregorian

to_from = int(input("1. To JDN\n2. From JDN\n"))


if to_from == 1:
    year = int(input("Year: "))
    month = int(input("Month: "))
    day = int(input("Day: "))

    jdn = gregorian_to_jdn.to_jdn(year, month, day)
    print("JDN:", jdn)

else:
    jdn = int(input("JDN: "))

    date = from_jdn_gregorian.from_jdn(jdn)
    print("Gregorian:", date)
