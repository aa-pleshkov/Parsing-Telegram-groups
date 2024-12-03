from datetime import datetime
import pytz
from telegram_client import connecting_to_telegram_client
from get_list_of_groups import get_list_of_groups
from get_list_of_groups import selecting_the_required_group
from get_latest_messages import get_latest_messages_from_selected_group
import csv
 
api_id = 24731930
api_hash = "984a7450c2014c7576cde3f193d1bf85"
phone = "+77087106072"

client = connecting_to_telegram_client(phone, api_id, api_hash)
client.start()

groups = get_list_of_groups(client)

target_group = selecting_the_required_group(groups)

timezone = pytz.timezone('Europe/Moscow')
start_date = timezone.localize(datetime(2024, 12, 2))
print(start_date)

all_messages = get_latest_messages_from_selected_group(client, target_group, timezone, start_date)

with open("chats.csv", "w", encoding="UTF-8") as f:
   writer = csv.writer(f, delimiter=",", lineterminator="\n")
   for message in all_messages:
       writer.writerow([message])

print('Парсинг сообщений группы успешно выполнен.')