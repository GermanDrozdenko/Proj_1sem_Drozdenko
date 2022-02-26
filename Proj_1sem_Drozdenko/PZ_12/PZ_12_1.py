# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать его в IDE PyCharm Community
# с применением пакета tk. Получить интерфейс максимально приближенный к оригиналу.
# Вариант 6

from tkinter import *
from tkinter import ttk

#конфигурация окна
root = Tk()
root.title("EVENT REGISTRATION FORM")
root.geometry('800x750')
root.configure(bg="White")
root.resizable(False, False)

#верхняя надпись
erg = Label(text="EVENT REGISTRATION FORM", bg="Black", font="Arial 18", fg="White", width=57, height=1, bd=10)
erg.place(x=0, y=1)

#текст name
name = Label(text="Name", bg="White", font="Arial 14", fg="Black")
name.place(x=60, y=90)

#текст company и поле для ввода
company = Label(text="Company", bg="White", font="Arial 14", fg="Black")
company.place(x=60, y=200)
cm = Entry(bg="LightGrey", fg="Black", width=48, font="Arial 14", bd=5)
cm.place(x=170, y=198)

#текст email и поле для ввода
email = Label(text="Email", bg="White", font="Arial 14", fg="Black")
email.place(x=60, y=290)
em = Entry(bg="LightGrey", fg="Black", width=48, font="Arial 14", bd=5)
em.place(x=170, y=288)

#текст phone
phone = Label(text="Phone", bg="White", font="Arial 14", fg="Black")
phone.place(x=60, y=380)

#текст subject
subject = Label(text="Subject", bg="White", font="Arial 14", fg="Black")
subject.place(x=60, y=480)

#список выбора опций
list1 = ["Math", "IT", "Science", "Economics", "Law"]
valueInside = StringVar(root)
valueInside.set("Choose option")
optionMenu = OptionMenu(root, valueInside, *list1)
optionMenu.configure(width=80)
optionMenu.pack()
optionMenu.place(x=170, y=480)

#текст first name и поле для ввода
firstName = Label(text="First Name", bg="White", font="Arial 11", fg="Grey")
firstName.place(x=170, y=125)
fn = Entry(bg="LightGrey", fg="Black", width=25, font="Arial 14", bd=5)
fn.place(x=170, y=90)

#текст last name и поле для ввода
lastName = Label(text="Last Name", bg="White", font="Arial 11", fg="Grey")
lastName.place(x=480, y=125)
ln = Entry(bg="LightGrey", fg="Black", width=20, font="Arial 14", bd=5)
ln.place(x=480, y=90)

#текст area code и поле для ввода
areaCode = Label(text="Area Code", bg="White", font="Arial 11", fg="Grey")
areaCode.place(x=170, y=415)
ac = Entry(bg="LightGrey", fg="Black", width=8, font="Arial 14", bd=5)
ac.place(x=170, y=378)

#текст phone number и поле для ввода
phoneNumber = Label(text="Phone Number", bg="White", font="Arial 11", fg="Grey")
phoneNumber.place(x=300, y=415)
pn = Entry(bg="LightGrey", fg="Black", width=20, font="Arial 14", bd=5)
pn.place(x=300, y=378)

#текст вопроса
question = Label(text="Are you an existing customer?", bg="White", font="Arial 13", fg="Black")
question.place(x=60, y=570)

#галочка yes
chkYes = Radiobutton(root, text="Yes", font="Arial 11", bg="White", value=0)
chkYes.place(x=60, y=600)

#галочка no
chkNo = Radiobutton(root, text="No", font="Arial 11", bg="White", value=1)
chkNo.place(x=160, y=600)

#кнопка register
btn = Button(root, bg="Red", fg="White", text="REGISTER", font="Arial 13", width=15, height=1, bd=5)
btn.place(x=62, y=650)

root.mainloop()