import os
from dotenv import load_dotenv, find_dotenv
from loger.logger_helper import get_logger

log = get_logger(__name__)

if not find_dotenv():
    log.info("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
# API_TOKEN = os.getenv("API_TOKEN")

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
ADD_CLIENT_URL = os.getenv("ADD_CLIENT_URL")
GET_INBOUNDS_URL = os.getenv("GET_INBOUNDS_URL")
AUTH_URL = os.getenv("AUTH_URL")

DATABASE_URL = os.getenv("DATABASE_URL")
BACK_DIR = os.path.abspath("main.py")
DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_USER = os.getenv("DB_USER")

ADMIN_ID = os.getenv("ADMIN_ID")
CHANNEL_URL = os.getenv("CHANNEL_URL")

DEV_MODE = True
YOOKASSA_SECRET_KEY = os.getenv("YOOKASSA_SECRET_KEY")
YOOKASSA_SHOP_ID = os.getenv("YOOKASSA_SHOP_ID")
CRYPTO_BOT_ENABLE = False
FREEKASSA_ENABLE = False
LEGACY_ENABLE = False
ROBOKASSA_ENABLE = False
SUB_PATH = None
YOOKASSA_ENABLE = False
REFERRAL_BONUS_PERCENTAGES = {
    "1": "0.10",  # 10% для первого уровня
    "2": "0.05",  # 5% для второго уровня
    "3": "0.02"   # 2% для третьего уровня
}
TOTAL_GB = 50

WEBHOOK_HOST = os.getenv("WEBHOOK_HOST")
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
SUPPORT_CHAT_URL = os.getenv("SUPPORT_CHAT_URL")
WEBAPP_HOST = os.getenv("WEBAPP_HOST")
WEBAPP_PORT = os.getenv("WEBAPP_PORT")
BACKUP_TIME = 86400


CONNECT_ANDROID = "https://goo.su/0H6Zf4q"
CONNECT_IOS = "https://goo.su/udjfGE"
DOWNLOAD_ANDROID = "https://goo.su/0H6Zf4q",
DOWNLOAD_IOS = "https://goo.su/udjfGE"
RENEWAL_PRICES = {"Месяц": "Бесплатно"}
TRIAL_TIME = 30

SERVERS = {"1": {}}



DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Список команд"),
)

