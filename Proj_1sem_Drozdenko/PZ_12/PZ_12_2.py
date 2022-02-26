# Разработать программу с применением пакета tk, взяв в качестве условия любую задачу из ПЗ №3-8
# Вариант 6. Смоделировать простейший калькулятор, умеющий выполнять 4 основные арифметические операции.

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Simple calculator")
root.geometry('400x300')
root.configure(bg="White")
root.resizable(False, False)

def result():
    messagebox.showinfo("Результат", eval(emp.get()))

emp = StringVar()

example = Label(text="Введите простое выражение:", bg="White", font="Arial 11", fg="Black")
example.place(x=10, y=10)
fn = Entry(bg="LightGrey", fg="Black", width=30, font="Arial 11", bd=2, textvariable=emp)
fn.place(x=10, y=35)


btn = Button(root, text="Посчитать", bg="LightGrey", fg="Black", font="Arial 11", bd=2, command=result)
btn.place(x=260, y=30)

root.mainloop()