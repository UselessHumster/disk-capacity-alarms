import os
import requests
import subprocess as sb
from src.config import BOT_TOKEN, CHAT_ID, DISKS_TO_CHECK, HOSTNAME
from src.install import install

IS_CONFIG = os.path.isfile(f'.env')

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
    link = f'https://api.telegram.org/{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}'
    response = requests.get(link)
    print( response.json())



def main():
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

