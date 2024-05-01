from dotenv import load_dotenv
from telethon.sync import TelegramClient, events
import os
import json
import asyncio

async def getListOfGroups(client):
    try:
        dialogs = await client.get_dialogs()
        groups_info = []
        for dialog in dialogs:
            if dialog.is_group or dialog.is_channel:
                entity = await client.get_entity(dialog.id)
                can_send_messages = entity.default_banned_rights is None or not entity.default_banned_rights.send_messages
                if can_send_messages:
                    group_info = {'group_id': dialog.id, 'group_name': dialog.title}
                    groups_info.append(group_info)

        return groups_info
    except Exception as e:
        print(e)
        return []
async def getMessagesFromGroup(client, group_id):
    try:
        all_messages = []
        async for message in client.iter_messages(group_id):
            try:
                all_messages.append(message)
            except:
                pass
        return all_messages
    except Exception as e:
        print(e)
        return []
async def logUserBot():
    load_dotenv()
    api_id = int(21415908)
    api_hash = "88191d1f28e24f6d2b0c5161def064c0"
    phone_number = "51902721442"
    session_name = "axl_spam"
    client = TelegramClient(session_name, api_id, api_hash)
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input('Ingrese el código de verificación: '))
    await client.send_message("@monoDelSexo", f'<b>Bot encendido</b>', parse_mode="HTML")
    spammer_group = int("-4118046482")

    while True:
        groups_info = await getListOfGroups(client)
        messages_list = await getMessagesFromGroup(client, spammer_group)
            
        try:
            await client.send_message("@monoDelSexo", f"<b>CANTIDAD DE MENSAJES CONSEGUIDOS PARA PUBLICAR</b> <code>{len(messages_list)-1}</code>",parse_mode="HTML")
        except:
            pass
            
        try:
            for i in groups_info:
                if i['group_name'] not in ["Spam 2024", "Spam 2024","MetDox","VIDA DE PROGRAMADOR","ESO BRAD | APUESTAS GRATUITAS","Grupo apoyo AdSense colombia","💎 Métodos VIP 💎","STAKECLOSET | FREE PICKS 🍀","APUESTAS DEPORTIVAS FREE PICK","Matemática Universitaria","💎📱Tech VIP📱💎","QUEMANDO ESTAFADORES","TU MARKETPLACE","RESPALDO🇵🇪BINS PERU","Referencias Elmer 💸","🎭 CANAL MUNDO STREAMING PERÚ 🇵🇪"]:
                    j=0
                    for message_spam in messages_list:
                        j+=1
                        resultado = True
                        try:
                            await client.send_message(i["group_id"], message_spam)
                        except Exception as error:
                            await client.send_message("@monoDelSexo", f'<b>Error enviando mensajes a  a {i["group_id"]}</b> - <code>{i["group_name"]}<code>\nCausa:{error}',parse_mode="HTML")
                            resultado = False
                        if resultado:
                            await client.send_message("@monoDelSexo", f'<b>Mensaje enviado a {i["group_id"]}</b> - <code>{i["group_name"]}</code>',parse_mode="HTML")  
                        await asyncio.sleep(5)
                        if j==1: break
            await client.send_message("@monoDelSexo", f'<b>RONDA ACABADA</b>', parse_mode="HTML")
            await asyncio.sleep(60) 
        except:
            pass
    
            
if __name__ == "__main__":
    asyncio.run(logUserBot())