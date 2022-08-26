import  time
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import FloodWaitError
from app_config import API_ID, API_HASH

channels=['TelethonChat', 'ru_python_beginners', 'pydjango']

with TelegramClient('telegram_session', API_ID, API_HASH) as client:
    for channel in channels:
        try:
            client(JoinChannelRequest(channel))
        except FloodWaitError as fwe:
            print(fwe)
            time.sleep(fwe.second+20)
        except Exception as e:
            print(e)