from pyrogram import *
from pyrogram.filters import regex, text_filter
from pyrogram.methods.utilities.start import Start
import logging
from pyrogram.handlers import *
from plugin.search_hentai import hentaisearch
from plugin.info_hentai import infohentai
from plugin.video_hentai import hentailink, hentaidl
from plugin.start import start
import os
import re

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)


API_ID = "10247139" 
API_HASH = "96b46175824223a33737657ab943fd6a"
BOT_TOKEN = "6663238213:AAG78z9yDGGYPP7Eh9EnsRI4okSQCol0whw"

bot = Client(
    "comic",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

def main():
    bot.add_handler(MessageHandler(hentaisearch, filters.regex(r'search')), group=1)
    bot.add_handler(CallbackQueryHandler(hentaidl, filters.regex('dlt_*')), group=5)
    bot.add_handler(CallbackQueryHandler(infohentai, filters.regex('info_*')), group=2)
    bot.add_handler(CallbackQueryHandler(hentailink, filters.regex('link_*')), group=6)
    bot.add_handler(MessageHandler(start , filters.regex(r'start')), group=13)


if __name__ == '__main__':
    bot.run(main())

