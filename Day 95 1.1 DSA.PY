def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

N = int(input().strip())

year = N
while not is_leap_year(year):
    year += 1

print(year)