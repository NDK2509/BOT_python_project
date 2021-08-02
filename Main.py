from random import sample
from datetime import time
from tkinter import *
from tkinter import ttk

#Constant
MON = 0
TUE = 1
WED = 2
THU = 3
FRI = 4
SAR = 5
SUN = 6
DAY_OF_WEEK = 7
#-------------------------------------------------
class Work:
    def __init__(self, work, time):
        self._work = work
        self._time = time
    def getWork(self):
        return self._work
    def setWork(self, newWork):
        self._work = newWork
    def getTime(self):
        return self._time
    def setTime(self, newTime):
        self._time = newTime
    def show(self):
        print('Work name:', self._work,', time:', self._time)

def timeTable(toDoList):
    def odd(n):
        if (n % 2 == 0): return False
        return True

    mark = [[],[],[],[],[],[],[]]

    for day in range(DAY_OF_WEEK):
        works_a_day = len(toDoList[day])
        n = works_a_day//2
        if (odd(works_a_day)):
            work_per_person = sample([n, n + 1], k = 2, counts = [1,1])
        else:
            work_per_person = [n, n]
        mark[day] = sample([True, False], k = works_a_day, counts = work_per_person)
    
    return mark

def sortTime(toDoList):
    def sort(list_work):
        for i in range(len(list_work)-1):
            for j in range(len(list_work)-i-1):
                if list_work[j].getTime() > list_work[j+1].getTime():
                    list_work[j], list_work[j+1] = list_work[j+1], list_work[j]
    for day in range(DAY_OF_WEEK):
        sort(toDoList[day])
        
def addWork(toDoList, day, work):
    toDoList[day].append(work)

def index_day(day):
    if day == 'Mon': return MON
    elif day == 'Tue': return TUE
    elif day == 'Wed': return WED
    elif day == 'Thu': return THU
    elif day == 'Fri': return FRI
    elif day == 'Sar': return SAR
    elif day == 'Sun': return SUN
def showToDo(toDoList):
    for day in range(DAY_OF_WEEK):
        print(day,":")
        for work in toDoList[day]:
            work.show()
#---------------------begin------------------------

toDoList = [[],[],[],[],[],[],[]]
mark = list()

