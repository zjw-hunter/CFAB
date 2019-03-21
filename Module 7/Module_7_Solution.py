import datetime
import random

currently = datetime.date.today()

targetMonth = random.randint(datetime.date.today().month + 1, 12)

dateMax = 0
if( targetMonth == 2 ):
    dateMax = 28
elif( targetMonth == 4 or targetMonth == 6 or targetMonth == 9 or targetMonth == 11):
    dateMax = 30
else:
    dateMax = 31

targetDay = random.randint(1, dateMax)

targetDate = datetime.date(2019, targetMonth, targetDay)

print("Today is: ", datetime.date.today())
print("My target date is: ", targetDate)
print("Time until the target date: ", targetDate - datetime.date.today())