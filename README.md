# Disk Capacity Alarms Script

## Функционал
Бот берет данные из строки df-h, парсит их и присылает в телеграм




## Настройка
Установка:

```
git clone https://github.com/UselessHumster/Disk-capacity-alarms.git
curl -LsSf https://astral.sh/uv/install.sh | sh
cd Disk-capacity-alarms
uv run main.py
```
При первом запуске происходит настройка бота

Скрипт запросит:
- токен
- ID чата куда слать данные
- какие диски или дирректории проверять


Добавить в cron:

- Вместо scripts указать дирректорию где лежит репозиторий
- Если требуется вместо root указать из под кого будет запускаться cron
- Поменять время если требуется (по умолчанию каждый день в 8 утра)

```
echo "0 8 * * * uv run /scripts/Disk-capacity-alarms/main.py >> /var/log/disk-capacity-py.log" >> /var/spool/cron/crontabs/root
```
