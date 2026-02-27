# Python code below
# Use print("messages...") to debug your solution.
import calendar

show_expected_result = False
show_hints = False

def count_days(year, month, whichday):
    # Your code goes here.
    cal = calendar.monthcalendar(year, month)
    count = 0
    for w in range(0, len(cal)):
        weektest = cal[w]
        if whichday == 0:
            day = weektest[calendar.MONDAY]
        elif whichday == 1:
            day = weektest[calendar.TUESDAY]
        elif whichday == 2:
            day = weektest[calendar.WEDNESDAY]
        elif whichday == 3:
            day = weektest[calendar.THURSDAY]
        elif whichday == 4:
            day = weektest[calendar.FRIDAY]
        elif whichday == 5:
            day = weektest[calendar.SATURDAY]
        else:
            day = weektest[calendar.SUNDAY]
        if day != 0:
            count += 1
    return count

def alt_sol(year, month, whichday):
    # Your code goes here.
    weekslist = calendar.monthcalendar(year, month)
    count = 0
    for w in weekslist:
        if w[whichday] != 0:
            count += 1
    return count

print(count_days(2026, 2, 0))
print(alt_sol(2026, 2, 0))