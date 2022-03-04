import requests
from telegram.bot import Bot
import time

BotToken = None
ChannelUsername = None # it could chat id

while True:
    try:
        with open('Result.jpg', 'wb') as File: File.write(requests.get("https://thispersondoesnotexist.com/image").content)
        Bot(BotToken).send_photo(chat_id=ChannelUsername, photo=open("Result.jpg", "rb"))
    except: pass

    time.sleep(10)
