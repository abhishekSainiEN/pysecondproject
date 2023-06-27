#python dateTime,time and calendar module

import datetime
import calendar

import time


print("abhi digital calendar")





def showCalendarofmonth(a,b):
    s=calendar.month(a,b)
    print(s)



def showCalendarofYear(a):
    s=calendar.prcal(a)
    print(s)

def currentTime():
    print(time.asctime(time.localtime(time.time())))

def currentDate():
    print(datetime.datetime.now())

def createOwnDate(a,b,c):
    s=datetime.datetime(a,b,c)
    print(s)


print("1 for print calendar of year:")
print("2 for print calendar of month:")
print("3 for print currentTime:")
print("4 for print currentDate:")
print("5 for print own predefined date:")

a=int(input("give number to choose what you want to perform:"))


if a==1:
    print("calendar:")

    year=int(input("give year:"))
    print("calendar:",year)

    showCalendarofYear(year)

elif a==2:
    print("calendar")
    year = int(input("give year:"))
    month =int(input("give month:"))
    print("calendar:",year,"",month)
    showCalendarofmonth(year,month)

elif a==3:
    print("currentTime:")
    currentTime()
elif a==4:
    print("currentDate:")
    currentDate()
elif a==5:
    print("own predefined date:")
    year = int(input("give year:"))
    month = int(input("give month:"))
    day=int(input("give day:"))
    createOwnDate(year,month,day)
else:
    print("invalid option")