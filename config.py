# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("24497690", ""))
API_HASH = getenv("fcdf57fd911834f83aaf42f15fbcb200", "")
BOT_TOKEN = getenv("8328547357:AAHMjd31wXXXAegOZ4Hx-sFUFg8ttUQjC8k", "")
OWNER_ID = list(map(int, getenv("8333847915", "6502857759", "").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("1003534327381", "")
CHANNEL_ID = int(getenv("1003534327381", ""))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "1000"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
