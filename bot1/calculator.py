import telebot

Api_token = '5468351287:AAHr0q5RLrycvoEpVVauIAnMTLc9bwkvplw'

bot = telebot.TeleBot(Api_token)
rkm = telebot.types.InlineKeyboardMarkup()
rkm.row(telebot.types.InlineKeyboardButton('c', callback_data='c'),
        telebot.types.InlineKeyboardButton('()', callback_data='()'),
        telebot.types.InlineKeyboardButton('%', callback_data='%'),
        telebot.types.InlineKeyboardButton('+', callback_data='+'))

rkm.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
        telebot.types.InlineKeyboardButton('8', callback_data='8'),
        telebot.types.InlineKeyboardButton('9', callback_data='9'),
        telebot.types.InlineKeyboardButton('*', callback_data='*'))

rkm.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
        telebot.types.InlineKeyboardButton('5', callback_data='5'),
        telebot.types.InlineKeyboardButton('6', callback_data='6'),
        telebot.types.InlineKeyboardButton('-', callback_data='-'))

rkm.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
        telebot.types.InlineKeyboardButton('2', callback_data='2'),
        telebot.types.InlineKeyboardButton('3', callback_data='3'),
        telebot.types.InlineKeyboardButton('/', callback_data='/'))

rkm.row(telebot.types.InlineKeyboardButton('+/-', callback_data='(-'),
        telebot.types.InlineKeyboardButton('0', callback_data='0'),
        telebot.types.InlineKeyboardButton('.', callback_data='.'),
        telebot.types.InlineKeyboardButton('=', callback_data='='))

value = ''
old_value = ''


@bot.message_handler(commands=['start'])
def welcome(message):
    global value
    if value == '':
        bot.send_message(message.from_user.id, '0', reply_markup=rkm)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=rkm)


@bot.callback_query_handler(func=lambda call: True)
def callback_func(message):
    global value, old_value

    if message.data == '=':
        try:
            value = str(eval(value))
        except:
            value = "Dasturdan Xato Foydalanayapsiz"
    elif message.data == 'c':
        value = ''

    else:
        value += message.data

    if value != old_value:
        if value == '':
            bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.id, text='0',
                                  reply_markup=rkm)
        else:
            bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.id, text=value,
                                  reply_markup=rkm)
    old_value = value


bot.polling(none_stop=False, interval=0)
