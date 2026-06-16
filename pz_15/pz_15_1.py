#Приложение БЮРО ПО ТРУДОУСТРОЙСТВУ для некоторой организации.
#БД должна содержать таблицу Работник со следующей структурой записи:
#фамилия, имя, отчество, возраст, пол, профессия, стаж работы.

import sqlite3 as sq

scheme = """
create table if not exists worker (
    id integer primary key autoincrement,
    name  text not null,
    surname text not null,
    patronymic text not null,
    age integer not null,
    sex integer not null,
    workplace text not null,
    experience integer not null
);
"""
dbname = "worker.db"

def create():
    with sq.connect(dbname) as con:
        cur = con.cursor()
        cur.execute(scheme)

def get(id):
    with sq.connect(dbname) as con:
        cur = con.cursor()
        cur.execute("select * from worker where id = ?", (id,))
        return cur.fetchone()

def insert(name, surname, patronymic, age, sex, workplace, experience):
    with sq.connect(dbname) as con:
        cur = con.cursor()
        cur.execute(
            "insert into worker values (null, ?,?,?,?,?,?,?)",
            (name, surname, patronymic, age, sex, workplace, experience),
        )

def execute(sql):
    with sq.connect(dbname) as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

def update(id, name, surname, patronymic, age, sex, workplace, experience):
    with sq.connect(dbname) as con:
        cur = con.cursor()
        cur.execute(
            "update worker set name = ?, surname = ?, patronymic = ?, age = ?, sex = ?, workplace = ?, experience = ? where id = ?",
            (name, surname, patronymic, age, sex, workplace, experience, id),
        )

def delete(id):
    with sq.connect(dbname) as con:
        cur = con.cursor()
        cur.execute("delete from worker where id = ?", (id,))

create()

insert("Maxim", "Kotlinov", "test", 17, 1, "Programmer", 1)
insert("Stepan", "Bobov", "test", 27, 1, "Programmer", 3)
insert("Joe", "Govo", "test", 27, 1, "Programmer", 3)
insert("Suzie", "Trom", "test", 27, 1, "Programmer", 3)
insert("Nikolai", "Sxdaz", "test", 27, 1, "Programmer", 3)
insert("Maria", "Chinese", "test", 27, 1, "Programmer", 3)
insert("Daria", "Popov", "test", 27, 1, "Programmer", 3)
insert("Alexander", "", "test", 27, 1, "Programmer", 3)
insert("Dmitri", "Bobov", "test", 27, 1, "Programmer", 3)
insert("Timofey", "Bobov", "test", 27, 1, "Programmer", 3)

print(get(1))
print(execute("select * from worker"))
update(1, "Maxim", "Kotlinov", "Alexandrovich", 18, 1, "Programmer", 2)
print(get(1))
delete(2)
print(execute("select * from worker"))