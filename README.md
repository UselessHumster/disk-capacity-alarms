# Disk Capacity Alarms Script

## Функционал
Скрипт берет данные из строки df-h, парсит их и присылает в телеграм




## Настройка
Установка:

```
git clone https://github.com/UselessHumster/disk-capacity-alarms.git
curl -LsSf https://astral.sh/uv/install.sh | sh
cd disk-capacity-alarms
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
echo "0 8 * * * uv run /scripts/disk-capacity-alarms/main.py > /var/log/disk-capacity-py.log > 2>&1" >> /var/spool/cron/crontabs/root
```


или вручную
```
EDITOR=nano crontab -e
0 8 * * * uv run /scripts/disk-capacity-alarms/main.py > /var/log/disk-capacity-py.log > 2>&1
```
