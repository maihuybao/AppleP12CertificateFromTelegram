from telethon import TelegramClient, events, sync
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




client = TelegramClient('Sessions/mohobo', config['api_id'], config['api_hash'])
client.start()
for message in client.get_messages(config['channel_username'], limit=100):
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
                client.download_media(message, file=f'{path}/Cert/{Cername}')
                # Assuming `rawMessage` contains the message text
                match = re.search(r'Esign Link:(.*)', rawMessage)
                if match:
                    esignURL = match.group(1).strip()
                match = re.search(r'Esign Link:(.*)', rawMessage)
                if match:
                    esignURL = match.group(1).strip()
                # print(esignURL)
                update_json(Cername, {"status": "Good", "esignURL": esignURL})
            else:
                #remove file
                os.remove(f'{path}/Cert/{Cername}')
                update_json(Cername, {"status": "Revoked"})
    except:
        pass
        
        
