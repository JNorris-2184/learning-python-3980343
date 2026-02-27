#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
#print(timedelta(days=365,hours=5,minutes=1))

# print today's date
now = datetime.now()
# print(now)

# print today's date one year from now
# print(now + timedelta(days=365))

# create a timedelta that uses more than one argument
# print(now + timedelta(weeks=2, days=3))

# calculate the date 1 week ago, formatted as a string
# t = datetime.now() - timedelta(weeks=1)
# s = t.strftime("%A %B %d %Y")
# print(s)

### How many days until April Fools' Day?
today = date.today()
afd = date(today.year,4,1)
if afd < today:
        print(f"already passed {(today-afd).days} days ago")
        afd = afd.replace(year=today.year+1)
time_to_afd = afd-today
print(f'Time to AFD {(afd-today).days}')