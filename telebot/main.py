import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

# Replace with your bot token
API_TOKEN = "7751070372:AAGr6nYdz2bd26RyjFaHvnUZeyMxl5K9IlE"
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    # Send the initial message
    bot.send_message(message.chat.id,
                     "🤗HELLO DEAR 😊\n"
                     "ON THIS BOT YOU CAN BUY FOOTBALL GAMES FOR FREE ONLY IN EXCHANGE🎇\n"
                     "👉 Use the following commands:\n"
                     "/coupons - Get Purchased Football Games Coupons\n"
                     "/about - About Me\n"
                     "/evidence - View Evidence")

@bot.message_handler(commands=['coupons'])
def coupons(message):
    bot.send_message(message.chat.id, "🌈FULFILL TERMS AND GET FREE COUPONS🌤")

@bot.message_handler(commands=['about'])
def about(message):
    bot.send_message(message.chat.id, (
        "🌐🌈MY NAME IS BEKNAZAR I USED TO WORK FOR 1WIN SECURITY AND I WAS FIRED FOR UNKNOWN REASONS\n"
        "NOW I GO TO THEIR DATABASE AND KNOW THE FOOTBALL GAMES THAT ARE SOLD, WHICH SLOTS GIVE MAX WIN WHEN\n"
        "AND I CONTINUE TO SHARE WITH PEOPLE. 🛑 ATTENTION 🛑!!! CURRENTLY 1WIN COMPANY IS BLOCKING MAX WIN WINNERS\n"
        "ACCOUNT I FOUND A SOLUTION AND CREATED A PROMO CODE AFTER YOU ENTER THIS PROMO CODE THEY CANNOT VERIFY YOU\n"
        "AND YOU CAN PAY ANY MONEY YOU WANT. CONTACT ME FOR PROMO CODE😎"
    ))

@bot.message_handler(commands=['evidence'])
def evidence(message):
    bot.send_message(message.chat.id, ("I HAVE SO MANY EVIDENCES LIKE THIS SORRY I CAN'T POST EVERYTHING ON THE BOT BECAUSE THE LIMITS ARE LESS.😔😔"))


# Start the bot
bot.polling(none_stop=True)
