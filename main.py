# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "dotenv",
#     "requests",
# ]
# ///
import os
import socket
import requests
import pathlib
import subprocess as sb
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = pathlib.Path(__file__).parent.resolve()
IS_CONFIG = os.path.isfile(f'{ROOT_DIR}/.env')
HOSTNAME=socket.gethostname()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
DISKS_TO_CHECK = os.getenv("DISKS_TO_CHECK")

def install():
    print('Конфигурации не найдено, давайте её создадим!')
    env = open(f'.env', "w+")
    env.write(f"BOT_TOKEN={input('Укажите токен бота: ')}\n")
    env.write(f"CHAT_ID={input('Укажите чат ID: ')}\n")
    env.write(f"DISKS_TO_CHECK={input('Укажите через пробел какие диски или дирректории проверять: ')}\n")
    env.close
    print('Конфигурация успешно создана! Запустите скрипт ещё раз')


def get_info():
    data = []
    for disk in DISKS_TO_CHECK.split(' '):
        cmd = f'df -h | grep {disk}'
        try:
            entry = sb.check_output(cmd, shell=True).decode("utf-8")
        except sb.CalledProcessError:
            print(f'No such disk as {disk}')
            continue
        data += entry.strip().split('\n')
    return data

def gen_text(disk_info):
    return f'{disk_info["name"]} free space: {disk_info["avail"]}; used: {disk_info["use%"]}'

def send(text):
    link = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}'
    response = requests.get(link)
    print( response.json())



def main():
    if BOT_TOKEN[:3] == 'bot':
        raise ValueError('Токен не должен содержать bot в начале, отредактируйте .env конфигурацию')
    output = get_info()
    data_to_send = f'Проверка хранилища на {HOSTNAME}\n\n'
    for disk in output:
        print(f'{disk=}')
        disk = [i for i in disk.split(' ') if i]
        disk_info = {'name': disk[0],
                     'size': disk[1],
                     'used': disk[2],
                     'avail': disk[3],
                     'use%': disk[4]}
        data_to_send += f'{gen_text(disk_info)}\n'
    send(data_to_send)



if __name__ == "__main__":
    if IS_CONFIG:
        main()
    else:
        install()

