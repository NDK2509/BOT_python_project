from random import sample
from datetime import time

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
    def __init__(self, work = str(), time = time()):
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

def timeTable(toDoList = list()):
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
def sortTimeTable(toDoList = list()):
    for day in range(DAY_OF_WEEK):
        sorted()
def addWork(toDoList, day, work):
    toDoList[day].append(work)

#---------------------begin------------------------
todo = [
    [Work('Watering', time(5,30)), Work('Cooking breakfast', time(6)), Work('Cooking', time(11,30)),Work('Picking child up', time(17,30))],
    [Work('Watering', time(5,30)), Work('Cooking breakfast', time(6)), Work('Cooking', time(11))],
    [Work('Watering', time(5,30)), Work('Cooking breakfast', time(6))],
    [Work('Watering', time(5,30)), Work('Cooking breakfast', time(6))],
    [Work('Watering', time(5,30)), Work('Cooking breakfast', time(6))],
    [Work('Watering', time(5,30)), Work('Cooking breakfast', time(6))],
    [Work('Watering', time(5,30)), Work('Cooking breakfast', time(6))]
]

addWork(todo, WED, Work('Laundry', time(21,30)))
todo[WED][2].show()
#mark = timeTable(todo)
#print(mark)
