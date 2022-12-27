import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5522140486:AAHZsPEQZyI1csyGxrv25ourtGlDZ01s1W8")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "11474352"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "efb8d26d9e2f91ff197b09c98aefca15")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001550147565"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1413812222"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "postgres://fsbntgyuwudejl:9572391865a408c8961af6fff8d0e2f5408f9012a8a4b0569856a11ad15ed2a6@ec2-44-206-45-169.compute-1.amazonaws.com:5432/d1mu90mf8b51ls")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001845536832"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1413812222 5531461861").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
