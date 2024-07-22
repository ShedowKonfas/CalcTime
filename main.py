from tkinter import *
from tkinter import messagebox

root = Tk()

def btn_click():
    try:
        days = eval(DaysInput.get())
        hours = eval(HoursInput.get())
        minutes = eval(MinutsInput.get())
        seconds = eval(SecondsInput.get())
        
        total_seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds
        days_result = total_seconds // 86400
        hours_result = (total_seconds % 86400) // 3600
        
        info_str = f'Результат: дней: {days_result} и часов: {hours_result}'
        messagebox.showinfo(title='Кол-во времени: ', message=info_str)
    except ValueError:
        messagebox.showerror(title='Ошибка', message='Введите целое число')

root.title("Time calculator")
root.geometry("300x350")

root.resizable(True, True)

canvas = Canvas(root, height=300, width=350)
canvas.pack()

frame = Frame(root)
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text="Введите количество дней", font=("Arial", 12))
title.pack()
DaysInput = Entry(frame)
DaysInput.pack()


title = Label(frame, text="Введите количество часов", font=("Arial", 12))
title.pack()
HoursInput = Entry(frame)
HoursInput.pack()


title = Label(frame, text="Введите количество минут", font=("Arial", 12))
title.pack()
MinutsInput = Entry(frame)
MinutsInput.pack()


title = Label(frame, text="Введите количество секунд", font=("Arial", 12))
title.pack()
SecondsInput = Entry(frame)
SecondsInput.pack()




btn = Button(frame, text="Расчёт", command=btn_click)
btn.pack()


root.mainloop()