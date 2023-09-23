import telebot
import random
from telebot import types
# Загружаем список интересных фактов
f = open('facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
# Загружаем список пирогов
f = open('pirogi.txt', 'r', encoding='UTF-8')
pirogi = f.read().split('\n')
f.close()
f = open('kto.txt', 'r', encoding='UTF-8')
kto  = f.read().split('\n')
f.close()
# Создаем бота
bot = telebot.TeleBot('6077522144:AAEscMyZppDtKlNMaNLIxtejAocer3xVPpM')
# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Действие")
        item2=types.KeyboardButton("Хочу пирог")
        item3 = types.KeyboardButton("Кто")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(m.chat.id, 'Нажми: \nДействие для выбора занятия\nХочу пирог — сам знаешь, когда ',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт
    if message.text.strip() == "Действие":
            answer = random.choice(facts)
    # Если юзер прислал 2, выдаем пирог
    elif message.text.strip() == "Хочу пирог":
            answer = random.choice(pirogi)
    elif message.text.strip() == "Кто":
        answer = random.choice(kto)
    elif message.text.strip():
        answer = " "
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)
# Запускаем ботаpython
bot.polling(none_stop=True, interval=0)