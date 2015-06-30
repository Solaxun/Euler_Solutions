def leapyear(date):
    if date.year%4==0 and date.year%400==0:
        return True
    elif date.year%4==0 and date.year%100!=0:
        return True

days = {'monday':0,'tuesday':1,'wednesday':2,'thursday':3,
        'friday':4,'saturday':5,'sunday':6}
import datetime
start=datetime.date(1901,1,1)
end=datetime.date(2000,12,31)

delta=end-start

alldays=[start+datetime.timedelta(i) for i in range(delta.days)]
mondays=[day for day in alldays if day.weekday() == 6 and day.day==1]
leapyears={day.year for day in alldays if leapyear(day)}

print(len(mondays))