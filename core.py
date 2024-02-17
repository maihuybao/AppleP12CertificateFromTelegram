from telethon import TelegramClient, events, sync
import asyncio
from dotenv import load_dotenv, dotenv_values
import os
import json
import re
import json



path = os.getcwd()
load_dotenv()
config = dotenv_values(".env")
config = dict(config)
json_file = open(f'{path}/status.json')
data = json.load(json_file)

# function to update json with key and value if not will create
def update_json(key, value):
    key = key.replace(".zip", "")
    data[key] = value
    with open(f'{path}/status.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)






async def refresh():
    global config
    client = TelegramClient("Sessions/"+config['session_name'], config['api_id'], config['api_hash'])
    await client.connect()
    for message in await client.get_messages(config['channel_username'], limit=100):
        #message.meida to json
        status = True
        # print("Revoked" in str(message.message))
        rawMessage = str(message.message)
        if ("Revoked" in rawMessage):
            status = False
        try:
            if message.media:
                Cername = message.media.document.attributes[0].file_name
                #continue if not file zip
                if (".zip" not in Cername):
                    continue
                if (status):
                    await client.download_media(message, file=f'{path}/Cert/{Cername}')
                    # Assuming `rawMessage` contains the message text
                    match = re.search(r'Esign Link:(.*)', rawMessage)
                    if match:
                        esignURL = match.group(1).strip()
                    match = re.search(r'Esign Link:(.*)', rawMessage)
                    if match:
                        esignURL = match.group(1).strip()
                    print(Cername,status)
                    update_json(Cername, {"status": "Good", "esignURL": esignURL})
                else:
                    #remove file
                    os.remove(f'{path}/Cert/{Cername}')
                    update_json(Cername, {"status": "Revoked"})
        except:
            pass
            
            
# asyncio.run(refresh())