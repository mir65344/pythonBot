import telebot
import random
TOKEN = '7175403166:AAFG4rdOoE_b6O2fC5Pjq6ovKfGioDQ6naU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Првиате")

@bot.message_handler(commands=['joke'])
def handle_joke(message):
    jokes = ['1', '33', '2', '4', '5']

    joke = random.choice(jokes)
    bot.send_message(message.chat.id, joke)

@bot.message_handler(commands=['fact'])
def handle_fact(message):
    facts = [
        'Самая крупная жемчужина в мире достигает 6 килограммов в весе.'
        'Законодательство США допускало отправку детей по почте до 1913 года.'
        'В языке древних греков не существовало слова, которое обозначало религию.'
        'В современной истории есть промежуток времени, когда на счетах компании «Apple», было больше средств, чем у американского правительства.'
        'В Монголии лишь в 1% площади живут люди'
    ]

    fact = random.choice(facts)
    bot.send_message(message.chat.id, fact)

bot.polling()

