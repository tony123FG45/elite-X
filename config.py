import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MAIN_GROUP_ID = int(os.getenv("MAIN_GROUP_ID"))
REFE_GROUP_ID = int(os.getenv("REFE_GROUP_ID"))
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID"))
SUPERADMIN_IDS = set(map(int, os.getenv("SUPERADMIN_IDS").split(',')))
AUTHORIZED_ADMIN_IDS = set(map(int, os.getenv("AUTHORIZED_ADMIN_IDS").split(',')))
API_URL = os.getenv("API_URL")
