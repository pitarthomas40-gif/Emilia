import orjson
import os


def get_user_list(config, key):
    with open("{}/Emilia/{}".format(os.getcwd(), config), "rb") as json_file:
        return orjson.loads(json_file.read())[key]

class Config(object):
    API_HASH = "79b81186aefef9ca9216c646152ffe45" # API_HASH from my.telegram.org
    API_ID = 32772113 # API_ID from my.telegram.org

    BOT_ID = 521 # BOT_ID
    BOT_USERNAME = "Gcmanager18_bot" # BOT_USERNAME

    MONGO_DB_URL = "mongodb+srv://rj5706603:O95nvJYxapyDHfkw@cluster0.fzmckei.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" # MongoDB URL from MongoDB Atlas

    SUPPORT_CHAT = "rosegroupsohman" # Support Chat Username
    UPDATE_CHANNEL = "rosebotsohman" # Update Channel Username
    START_PIC = "https://pic-bstarstatic.akamaized.net/ugc/9e98b6c8872450f3e8b19e0d0aca02deff02981f.jpg@1200w_630h_1e_1c_1f.webp" # Start Image
    DEV_USERS = [7028236763] # Dev Users
    TOKEN = "8392569167:AAEC2BmJhoax7eYi-C1hNcTvzPM9z9YMtGY" # Bot Token from @BotFather
    CLONE_LIMIT = 50 # Number of clones your bot can make

    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)

    EVENT_LOGS = --1003877180460 # Event Logs Chat ID
    OWNER_ID = 7028236763 # Owner ID
 
    TEMP_DOWNLOAD_DIRECTORY = "./" # Temporary Download Directory
    BOT_NAME = "Sohman bot" # Bot Name
    WALL_API = "6950f53" # Wall API from wall.alphacoders.com
    GROQ_API_KEY = "gsk_mm" # GROQ API Key from groq.com


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
