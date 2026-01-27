import orjson
import os


def get_user_list(config, key):
    with open("{}/Emilia/{}".format(os.getcwd(), config), "rb") as json_file:
        return orjson.loads(json_file.read())[key]


class Config(object):
    API_HASH = "79b81186aefef9ca9216c646152ffe45"
    API_ID = 32772113

    BOT_ID = 521
    BOT_USERNAME = "Gcmanager18_bot"

    MONGO_DB_URL = "mongodb+srv://rj5706603:O95nvJYxapyDHfkw@cluster0.fzmckei.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    SUPPORT_CHAT = "rosegroupsohman"
    UPDATE_CHANNEL = "rosebotsohman"
    START_PIC = "https://pic-bstarstatic.akamaized.net/ugc/9e98b6c8872450f3e8b19e0d0aca02deff02981f.jpg@1200w_630h_1e_1c_1f.webp"
    DEV_USERS = [7028236763]
    TOKEN = "8392569167:AAEC2BmJhoax7eYi-C1hNcTvzPM9z9YMtGY"
    CLONE_LIMIT = 50

    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)

    EVENT_LOGS = -1003877180460
    OWNER_ID = 7028236763

    TEMP_DOWNLOAD_DIRECTORY = "./"
    BOT_NAME = "Sohman bot"
    WALL_API = "6950f53"
    GROQ_API_KEY = "gsk_mm"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
