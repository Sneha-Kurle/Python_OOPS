# import datetime
# date=datetime.date(2025, 4, 6)
# date1=datetime.date.today()
# print(date1)

# #time
# time=datetime.time(22,45,34)
# now=datetime.datetime.now()
# now=now.strftime('%H:%M:%S' ' %Y-%m-%d')
# print(now)

#exersice
import datetime
target=datetime.datetime(2027,4,6, 6,30,0)
current=datetime.datetime.now()
if target<current:
    print('The time has passed')
else:
    print('The time has not passed')