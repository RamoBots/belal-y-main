import os
from os import getenv
from dotenv import load_dotenv
from OWNER import BOT_TOKEN, OWNER, OWNER_NAME, DATABASE, CHANNEL, GROUP, LOGS, PHOTO, VID_SO


load_dotenv()

load_dotenv()
admins = {}
user = {}
call = {}
dev = {}
logger = {}
logger_mode = {}
botname = {}
appp = {}
helper = {}



API_ID = int(getenv("API_ID", "24514467"))
API_HASH = getenv("API_HASH", "5a8c3d38c4d89b672062c5ff015380c7")
BOT_TOKEN = BOT_TOKEN
MONGO_DB_URL = DATABASE
OWNER = OWNER 
OWNER_NAME = OWNER_NAME
CHANNEL = CHANNEL
GROUP = GROUP
PHOTO = PHOTO
LOGS = LOGS
VID_SO = VID_SO
