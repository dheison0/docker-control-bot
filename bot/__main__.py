from telebot import TeleBot
from . import BOT_TOKEN

bot = TeleBot(BOT_TOKEN)

@bot.message_handler(["start"])
def start(msg):
    bot.reply_to(msg, "Hello World!")

bot.infinity_polling()