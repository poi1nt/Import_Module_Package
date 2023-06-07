from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
import aiogram
import telebot

if __name__ == '__main__':
    print(f'Текущее время {datetime.datetime.now().time()}')
    calculate_salary()
    get_employees()