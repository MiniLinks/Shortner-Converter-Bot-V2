# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "23761681"))
API_HASH = os.environ.get("API_HASH", "32c507b43fc4e2cadc492da6a5689805")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6277618881:AAFJGtTcZDUTrI1U0mEIGmfSJCIYyeal-LQ")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("6222046628")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Mini Links")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://MiniLinks:Saketh159@cluster0.oktgsyi.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "6222046628")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001877127446")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "MiniLinksOfficial") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
