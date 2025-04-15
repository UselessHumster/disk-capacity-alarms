import os
import socket
from dotenv import load_dotenv

load_dotenv()
HOSTNAME=socket.gethostname()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
DISKS_TO_CHECK = os.getenv("DISKS_TO_CHECK")
