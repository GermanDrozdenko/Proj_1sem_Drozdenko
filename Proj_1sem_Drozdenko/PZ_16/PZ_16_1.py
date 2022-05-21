# Приложение для туристического агентства ТУР. Таблица Турист должна
# содержать следующую информацию о клиентах турфирмы: Код клиента, Клиент
# (Фамилия), Телефон, Название страны, Регион, Продолжительность поездки,
# Стоимость путевки.
# БД должна обеспечить получение информации о клиентах по фамилии.


import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):

    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#F0F0F0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="plus.png")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить', command=self.open_dialog, bg='#FFFFFF', bd=0,
                                    compound=tk.TOP, width=70, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="edit.png")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#FFFFFF',
                                    bd=0, compound=tk.TOP, width=90, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="delete.png")
        btn_delete = tk.Button(toolbar, text="Удалить", command=self.delete_records, bg='#FFFFFF',
                                    bd=0, compound=tk.TOP, width=70, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="search.png")
        btn_search = tk.Button(toolbar, text="Поиск", command=self.open_search_dialog, bg='#FFFFFF',
                               bd=0, compound=tk.TOP, width=70, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="update.png")
        btn_refresh = tk.Button(toolbar, text="Обновить", command=self.view_records, bg='#FFFFFF',
                               bd=0, compound=tk.TOP, width=70, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('client_id', 'surname', 'phone', 'country', 'region', 'duration', 'price'), height=15, show='headings')

        self.tree.column('client_id', width=100, anchor=tk.CENTER)
        self.tree.column('surname', width=180, anchor=tk.CENTER)
        self.tree.column('phone', width=140, anchor=tk.CENTER)
        self.tree.column('country', width=140, anchor=tk.CENTER)
        self.tree.column('region', width=140, anchor=tk.CENTER)
        self.tree.column('duration', width=140, anchor=tk.CENTER)
        self.tree.column('price', width=140, anchor=tk.CENTER)

        self.tree.heading('client_id', text='Код клиента')
        self.tree.heading('surname', text='Клиент (Фамилия)')
        self.tree.heading('phone', text='Телефон')
        self.tree.heading('country', text='Страна')
        self.tree.heading('region', text='Регион')
        self.tree.heading('duration', text='Длительность')
        self.tree.heading('price', text='Стоимость')

        self.tree.pack()

    def records(self, client_id, surname, phone, country, region, duration, price):
        self.db.insert_data(client_id, surname, phone, country, region, duration, price)
        self.view_records()

    def update_record(self, client_id, surname, phone, country, region, duration, price):
        self.db.cur.execute("""UPDATE users SET client_id=?, surname=?, phone=?, country=?, region=?, duration=?, price=? WHERE client_id=?""",
                            (client_id, surname, phone, country, region, duration, price, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM users WHERE client_id=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    # def search_records(self, client_id):
    #     client_id = ("%" + client_id + "%",)
    #     self.db.cur.execute("""SELECT * FROM users WHERE surname LIKE ?""", client_id)
    #     [self.tree.delete(i) for i in self.tree.get_children()]
    #     [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def search_records(self, surname):
        surname = (surname,)
        self.db.cur.execute("""SELECT * FROM users WHERE surname=?""", surname)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]


    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()

class Child(tk.Toplevel):

    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить')
        self.geometry('400x270+400+300')
        self.resizable(False, False)
        self.iconphoto(False, tk.PhotoImage(file="tourist.png"))

        label_description = tk.Label(self, text='Номер')
        label_description.place(x=50, y=25)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=140, y=25)

        label_surname = tk.Label(self, text='Фамилия')
        label_surname.place(x=50, y=50)
        self.entry_surname = ttk.Entry(self)
        self.entry_surname.place(x=140, y=50)

        label_phone = tk.Label(self, text='Телефон')
        label_phone.place(x=50, y=75)
        self.entry_phone = ttk.Entry(self)
        self.entry_phone.place(x=140, y=75)

        label_country = tk.Label(self, text='Страна')
        label_country.place(x=50, y=100)
        self.entry_country = ttk.Entry(self)
        self.entry_country.place(x=140, y=100)

        label_region = tk.Label(self, text='Регион')
        label_region.place(x=50, y=125)
        self.entry_region = ttk.Entry(self)
        self.entry_region.place(x=140, y=125)

        label_duration = tk.Label(self, text='Длительность')
        label_duration.place(x=50, y=150)
        self.entry_duration = ttk.Entry(self)
        self.entry_duration.place(x=140, y=150)

        label_price = tk.Label(self, text='Стоимость')
        label_price.place(x=50, y=175)
        self.entry_price = ttk.Entry(self)
        self.entry_price.place(x=140, y=175)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=210)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=210)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_surname.get(),
                                                                       self.entry_phone.get(),
                                                                       self.entry_country.get(),
                                                                       self.entry_region.get(),
                                                                       self.entry_duration.get(),
                                                                       self.entry_price.get()))

        self.grab_set()
        self.focus_set()

class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=210)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.entry_surname.get(),
                                                                          self.entry_phone.get(),
                                                                          self.entry_country.get(),
                                                                          self.entry_region.get(),
                                                                          self.entry_duration.get(),
                                                                          self.entry_price.get()))
        self.btn_ok.destroy()

class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app
        self.iconphoto(False, tk.PhotoImage(file="tourist.png"))

    def init_search(self):
        self.title("Поиск")
        self.geometry("320x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Фамилия")
        label_search.place(x=40, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=155)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

class DB:
    def __init__(self):

        with sq.connect('tour.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                surname TEXT,
                phone INTEGER,
                country TEXT,
                region TEXT,
                duration INTEGER,
                price INTEGER
                )""")

    def insert_data(self, client_id, surname, phone, country, region, duration, price):
        self.cur.execute("""INSERT INTO users(client_id, surname, phone, country, region, duration, price) VALUES (?, ?, ?, ?, ?, ?, ?)""",
                             (client_id, surname, phone, country, region, duration, price))
        self.con.commit()

if __name__ == "__main__":
    root = tk.Tk()
    root.iconphoto(False, tk.PhotoImage(file="tourist.png"))
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Турист")
    root.geometry("1000x500+300+200")
    root.resizable(False, False)
    root.mainloop()