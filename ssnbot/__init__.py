import os
import re
import logging
import logging.config
from dotenv import load_dotenv

load_dotenv(override=True)

pattern = re.compile(r"^.\d+$")

# vars
APP_ID = os.environ.get("APP_ID", "28045580")
API_HASH = os.environ.get("API_HASH", "83001e24418ec7f54bfe95d4e390419f")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7476307432:AAESoS055Z4ixMzoiKS9x4YURy0gySKkERU")
DB_URL = os.environ.get("DB_URL", "")
OWNER_ID = int(os.environ.get('OWNER_ID', "655594746"))
MUST_JOIN = os.environ.get("MUST_JOIN", "https://t.me/Puthusa_yosi")
ADMINS = [
    int(user) if pattern.search(user) else user
    for user in os.environ.get("ADMINS", "961156494").split()
] + [OWNER_ID]


# logging Conf
logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
