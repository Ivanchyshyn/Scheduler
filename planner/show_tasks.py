"""
Выдает 5 следующих дел и 5 последних, которые прошли.
Считается относительно текущей даты.
Так же чтобы можно было в консоли параметром ввести на какой день считать вместо сегодняшнего.
"""
import datetime
import operator
import sqlite3


def print_tasks(tasks):
    if tasks:
        for task in tasks:
            print('{} {}'.format(*task))
    else:
        print('No tasks')
    print()


def show(day):
    try:
        conn = sqlite3.connect('planner.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM planner')
        date_format = '%d.%m.%Y'
        if day is None:
            today = datetime.datetime.now()
        else:
            today = datetime.datetime.strptime(day, date_format)
        tasks = []
        past_tasks = []
        future_tasks = []
        for name, date in cursor:
            date = datetime.datetime.strptime(date, date_format)
            if (date.year, date.month, date.day) == (today.year, today.month, today.day):
                tasks.append((name, date))
            elif date < today:
                past_tasks.append((name, date))
            else:
                future_tasks.append((name, date))
        past_tasks = sorted(past_tasks, key=operator.itemgetter(1), reverse=True)
        future_tasks = sorted(future_tasks, key=operator.itemgetter(1))
        print('Today tasks:')
        print_tasks(tasks)
        print('Past tasks:')
        print_tasks(past_tasks)
        print('Future tasks:')
        print_tasks(future_tasks)
    finally:
        if conn:
            conn.close()
