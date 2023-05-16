import telebot
from config import keys, TOKEN
from utils import CurrencyConverter, ConvertionExeption

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Привет, {message.chat.username}! Для вывода инструкции отправте  /help")

@bot.message_handler(commands=['help'])
def send_help(massage):
    text = "Чтобы начать работу введите команду в формате: \n <количество переводимой валюты>\
    <название валюты> <в какую валюту перевести> \n Чтобы посмотреть доступные валюты отправте: /values"
    bot.send_message(massage.chat.id, text )

@bot.message_handler(commands=['values'])
def send_currency(massege: telebot.types.Message):
    text = 'Доступные валюты:'
    for k in keys:
        text = '\n'.join((text, k))
    bot.reply_to(massege, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) !=3:
            raise ConvertionExeption('Некоректное число параметров')
        amount, quote, base = values
        result = CurrencyConverter.converter(amount, quote, base)
    except ConvertionExeption as e:
        bot.reply_to(message, f'Ошибка пользователя. \n {e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n {e}')
    else:
        bot.send_message(message.chat.id, result)

bot.polling(none_stop=True)
