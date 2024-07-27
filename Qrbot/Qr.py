from telethon.sync import TelegramClient, events,connection
from pyzbar.pyzbar import decode
from PIL import Image


api_id = 1234567
         
api_hash = "apihash"


client =  TelegramClient('name', api_id, api_hash)



@client.on(events.NewMessage())
async def handler(event):

    if event.media:
        if event.media.photo:
            await client.download_media(event.media, thumb=-1,file=str(event.media.photo.id))

            zan = decode(Image.open(str(event.media.photo.id)+".jpg"))
            
            if zan != []:
                await event.reply("The content of your QR code is: \n"+str(zan[0].data,encoding='utf-8') )
            else:
                await event.reply("No content found :(")
            return       
    elif event.message.message=="/start":
        await event.reply("hello  dear "+(await client.get_entity(event.sender_id)).first_name + "\nwelcome to our bot\nsend your Qrcode")            
        return
    
    
    await event.reply("plz send photo!",)


    
    


client.start()    
client.run_until_disconnected()
