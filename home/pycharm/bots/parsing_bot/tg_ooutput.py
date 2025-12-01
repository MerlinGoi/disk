import db as db
import mai as main
import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '7120089991:AAFa19gwHnvTXFOCPp3vMIoDQSBSWXiQKrk'
bot = telebot.TeleBot(TOKEN)

# Define a handler for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am telegram bot. Send me /result to see all parsed info!")



# Define a handler for text messages
@bot.message_handler(commands=['result'])
def echo_all(message):

    bot.reply_to(message, f"please entr the URL adress:('https://www.work.ua/ru/jobs-odesa/?page=2')")
    print(message.text)
    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        bot.reply_to(message, message.text)
        print(message.text)
    
    

# Start polling for new messages
bot.polling()
