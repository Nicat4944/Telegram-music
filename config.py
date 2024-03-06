from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/797be7b5b198fb29e7d1f.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/797be7b5b198fb29e7d1f.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("Söhbet Grupu", "https://t.me/Music494_bot")
SUPPORT_CHANNEL = getenv("Söhbet Kanalı", "https://t.me/Fast_Owner")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/797be7b5b198fb29e7d1f.jpg"
