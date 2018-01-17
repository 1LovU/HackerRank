# https://www.hackerrank.com/challenges/linkedin-practice-nested-logic/problem


# date,month,year = map(int,input().strip().split())
DueDate,DueMonth,DueYear = map(int,input().strip().split())

DayLate = date-DueDate
monthLate = month-DueMonth
yearLate = year-DueYear

if yearLate==0:
    if monthLate==0:
        if DayLate<=0:
            print(0)
        else:
            print(DayLate*15)
    elif monthLate < 0 :
        print(0)
    else:
        print(500*monthLate)
elif yearLate < 0:
    print(0)
else:
    print(10000)
    
