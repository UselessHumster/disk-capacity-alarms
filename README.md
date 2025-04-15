# Disk Capacity Alarms Script

### Бот берет данные из строки df-h, парсит их и присылает в телеграм


При первом запуске происходит настройка бота
Скрипт запросит:
- токен
- ID чата куда слать данные
- какие диски или дирректории проверять

Установка:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
uv run main.py
```

Добавить в cron:

```
echo "0 8 * * * cd /scripts/Disk-capacity-alarms/ | uv run --project /scripts/Disk-capacity-alarms/ /scripts/Disk-capacity-alarms/main.py > /var/log/disk-capacity-py.log" >> /var/spool/cron/crontabs/root
```
