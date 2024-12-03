from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

def get_list_of_groups(client):

    chats = []
    last_date = None
    chunk_size = 200

    result = client(GetDialogsRequest(
                offset_date=last_date,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=chunk_size,
                hash = 0
            ))
    
    chats.extend(result.chats)

    return chats


def selecting_the_required_group(chats):

    groups = []

    for chat in chats:
        try:
            if chat.megagroup== True:
               groups.append(chat)
        except:
            continue

    print("Вам следует выбрать нужную группу для сбора из нее сообщений.")

    i=0
    for g in groups:
        print(str(i) + "- " + g.title)
        i+=1

    g_index = input("Введите нужную цифру: ")
    target_group = groups[int(g_index)]

    return target_group