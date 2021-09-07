from ast import parse
import telebot
import schedule
#Sunday


all1 = {'Дима': '752872267', 'Паша': '629075242', 'Полина Кочеткова': '967925905', 'Виталик': '485433810', 'Витя': '1250087021', 'Полина Ковалева': '650761348', 'Леша': '751974761', 'Ваня': '701727602', 'Наташа': '461883085', 'Максим': '688659984', 'Антон': '1084801379', 'Егор Белявский': '1280128315', 'Никита': '1242174386'}
hostel = {'Паша': '629075242', 'Полина Кочеткова': '967925905', 'Дима': '752872267', 'Ваня': '701727602', 'Наташа': '461883085', 'Максим': '688659984', 'Антон': '1084801379', 'Егор Белявский': '1280128315', 'Никита': '1242174386'}
minsk = {'Егор Белявский':'1280128315', 'Виталик':'485433810', 'Леша':'751974761', 'Антон':'1084801379'}
TOKEN = '1827746031:AAGKqa_5XyWhcBYtCIZ_QxhcQdmaoIHcHWQ'
duty = ['@againTL @Tomasttt @greedann', '@Shuhmen @NiK1TA315', '@kowalskivarianty ', '@natarg @Fllloyd', '@Appolinapiya ', ]


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['all'])
def tag_all(message):
    tag = ""
    for key, value in all1.items():
        tag += '['+key+'](tg://user?id='+str(value)+')' + " "
    bot.send_message(message.chat.id, tag, parse_mode="Markdown")


@bot.message_handler(commands=['hostel'])
def tag_hostel(message):
    tag = ""
    for key, value in hostel.items():
        tag += '['+key+'](tg://user?id='+value+')' + " "
    bot.send_message(message.chat.id, tag, parse_mode="Markdown")


@bot.message_handler(commands=['minsk'])
def tag_minsk(message):
    tag = ""
    for key, value in minsk.items():
        tag += '['+key+'](tg://user?id='+str(value)+')' + " "
    bot.send_message(message.chat.id, tag, parse_mode="Markdown")


@bot.message_handler(commands=['duty'])
def duty(message):
    tag_duty = '[Полина](tg://user?id=967925905)'
    bot.send_message(message.chat.id, tag_duty, parse_mode="Markdown")


if __name__ == '__main__':
    bot.polling(none_stop=True)
