# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "21608308"))
	API_HASH = os.environ.get("API_HASH", "decdf8683a924e72220a94e49ed8d3ce")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6510386769:AAEwwp-CW_Z_JS6xiB9O4GKW-LiUGhPZ9fg")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "ThammuTv_T_bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001888985177"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1904146512"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://aadi:sonybravia@cluster0.q5jzwv8.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "ThammuTv_T")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", -1001705130956")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @T3shaM

👥 **Support Group:** [Linux Repositories](https://t.me/ThammuTV)

📢 **Updates Channel:** [Discovery Projects](https://t.me/ThammuTV)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @T3shaM

Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[Donate Now]() (PayPal)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
