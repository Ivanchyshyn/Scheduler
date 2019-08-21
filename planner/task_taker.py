"""
Задача:
Спрашивает у юзера какое задание он хочет добавить.
Вводится название и планируемое время в виде день.месяц.
Естественно, если пользователь в декабре написал задачу на январь - это на следующий год.
Так же чтобы можно было написать "завтра" или "послезавтра"
"""
import sqlite3


def create():
    try:
        conn = sqlite3.connect('planner.db')
        name = input('Enter task name: ')
        task_time = input('Enter task day (day.month.year): ')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS planner (name text, date text)')
        cursor.execute('INSERT INTO planner VALUES (?, ?)', (name, task_time))
        conn.commit()
    finally:
        if conn:
            conn.close()
