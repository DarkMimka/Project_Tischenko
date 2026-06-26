#В соответствии с номером варианта перейти по ссылке на прототип.
#Реализовать его в IDE PyCharm Community с применением пакета tk.
#Получить интерфейс максимально приближенный к оригиналу (см. таблицу 1).

#Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ №№ 1 – 9.

from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.pack(fill="both")
ttk.Label(frm, text="Testform", font="bold").grid(
    row=0, column=0, columnspan=2, sticky="w"
)

#Основной фрейм
frm1 = ttk.Frame(frm, relief="raised", padding=10)
frm1.grid(row=1, column=0)

#Ряд 0: Имя
ttk.Label(frm1, text="Name").grid(row=0, column=0, sticky="w")
ttk.Entry(frm1).grid(row=0, column=1, sticky="ew")

#Ряд 1: Пароль
ttk.Label(frm1, text="Password").grid(row=1, column=0, sticky="w")
ttk.Entry(frm1).grid(row=1, column=1, sticky="ew")

#Ряд 2: Гендер
ttk.Label(frm1, text="Gender").grid(row=2, column=0, sticky="w")
gender_frame = ttk.Frame(frm1)
gender_frame.grid(row=2, column=1, sticky="w")
ttk.Radiobutton(gender_frame, text="Male").pack()
ttk.Radiobutton(gender_frame, text="Female").pack()

#Ряд 3: Континент
ttk.Label(frm1, text="Continent").grid(row=3, column=0, sticky="w")
m = ttk.Menubutton(frm1, text="Please select...")
m.grid(row=3, column=1, sticky="w")
m.menu = Menu(m)
m["menu"] = m.menu
for continent in [
    "Eurasia",
    "Australia",
    "North America",
    "South America",
    "Africa",
    "Oceania",
    "Arctic",
]:
    m.menu.add_checkbutton(label=continent)

#Ряд 4: вкусности
ttk.Label(frm1, text="Meals").grid(row=4, column=0, sticky="w")
meals_frame = ttk.Frame(frm1)
meals_frame.grid(row=4, column=1, sticky="w")
ttk.Checkbutton(meals_frame, text="breakfast").pack()
ttk.Checkbutton(meals_frame, text="lunch").pack()
ttk.Checkbutton(meals_frame, text="dinner").pack()

#Ряд 5: Ремарка
ttk.Label(frm1, text="Remark").grid(row=5, column=0, sticky="w")
ttk.Entry(frm1).grid(row=5, column=1, sticky="ew")

#Ряд 6: Кнопки
btn_frame = ttk.Frame(frm)
btn_frame.grid(row=6, column=0, sticky="e")
ttk.Button(btn_frame, text="Cancel").pack(side="right")
ttk.Button(btn_frame, text="Send").pack(side="right")

root.mainloop()
