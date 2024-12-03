from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

def connecting_to_telegram_client(phone, api_id, api_hash):

    client = TelegramClient(phone, api_id, api_hash)

    return client