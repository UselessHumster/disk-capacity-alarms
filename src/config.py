import os
import socket
from dotenv import load_dotenv

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
IS_CONFIG = os.path.isfile(f'{ROOT_DIR}/.env')

load_dotenv()
HOSTNAME=socket.gethostname()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
DISKS_TO_CHECK = os.getenv("DISKS_TO_CHECK")
