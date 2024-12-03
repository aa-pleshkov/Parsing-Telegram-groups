from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel

def get_latest_messages_from_selected_group(client, target_group, timezone, start_date):

    offset_id = 38000
    limit = 50
    all_messages = []
    total_messages = 0
    total_count_limit = 0

    while True:
        history = client(GetHistoryRequest(
            peer=target_group,
            offset_id=offset_id,
            offset_date=None,
            add_offset=0,
            limit=limit,
            max_id=0,
            min_id=0,
            hash=0
        ))

        if not history.messages:
            break

        messages = history.messages

        for message in messages:

            if message.date.tzinfo is None:
                message_date = timezone.localize(message.date)
            else:
                message_date = message.date.astimezone(timezone)

            if message_date >= start_date:    
                all_messages.append(str(message_date) + ' - ' + message.message)

        offset_id = messages[len(messages) - 1].id

        if total_count_limit != 0 and total_messages >= total_count_limit:
            break

    return all_messages