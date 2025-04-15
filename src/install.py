import os
import subprocess as sb
from .config import ROOT_DIR

def install():
    print('Конфигурации не найдено, давайте её создадим!')
    env = open(f'{ROOT_DIR}/.env', "w+")
    env.write(f"BOT_TOKEN={input('Укажите токен бота: ')}\n")
    env.write(f"CHAT_ID={input('Укажите чат ID: ')}\n")
    env.write(f"DISKS_TO_CHECK={input('Укажите через пробел какие диски или дирректории проверять: ')}\n")
    env.close
    print('Конфигурация успешно создана! Запустите скрипт ещё раз')
