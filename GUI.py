from tkinter import *
from tkinter import ttk
from Main import *
from datetime import *



def enter():
    day_list = days_entry.get().split(',')
    work = work_entry.get()
    time_list = time_entry.get().split(':')
    hour = int(time_list[0])
    min = int(time_list[1])
    Work(work, time(hour, min)).show()
    for day in day_list:
        addWork(toDoList, index_day(day), Work(work, time(hour, min)))
    
def divide():
    sortTime(toDoList)
    mark = timeTable(toDoList)
    showMark(mark)
    showWho(toDoList,mark)
def delete():
    resetToDo()
    resetMark()
    showToDo(toDoList)
    print(mark)
    print('Deleted successfully!')

root = Tk();
root.title("Time Table")

FONT = ('Arial', 20)
BG_COLOR = '#219ebc'

root.config(bg = BG_COLOR)

label_TimeTable = Label(root, text = "Time Table", font = FONT )
label_TimeTable.grid(row = 0, column = 2, padx = 10, pady = 10)
label_day = Label(root, text = "Day", font = FONT, background = '#219ebc')
label_day.grid(row = 1, column = 0, padx = 10, pady = 10)
label_work = Label(root, text = "Work", font = FONT, background = '#219ebc')
label_work.grid(row = 1, column = 2, padx = 10, pady = 10)
label_time = Label(root, text = "Time", font = FONT, background = '#219ebc')
label_time.grid(row = 1, column = 5, padx = 10, pady = 10)

days_entry = Entry(root, font = FONT, width = 15)
days_entry.grid(row=2, column=0, padx=10, pady=10)
work_entry = Entry(root, font = FONT, width = 15)
work_entry.grid(row=2, column=2, padx=10, pady=10)
time_entry = Entry(root, font = FONT, width = 15)
time_entry.grid(row=2, column=5, padx=10, pady=10)


enter_button = Button(root, 
    text='Enter', 
    bg='#e9c46a',
    font = ('Arial', 15),
    command = enter
)
enter_button.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

divide_button = Button(root, 
    text='Devide', 
    bg='#e9c46a',
    font = ('Arial', 15),
    width = 20,
    command = divide
)
divide_button.grid(row=4, column=0, padx=10, pady=10)

delete_button = Button(root, 
    text='Delete', 
    bg='#e9c46a',
    font = ('Arial', 15),
    width = 20,
    command = resetToDo, resetMark
)
delete_button.grid(row=4, column=5, padx=10, pady=10)

root.mainloop()