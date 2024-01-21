import telebot
from dotenv import load_dotenv
import os
from data import clock_emoji, book_emoji
from create_button_func import create_inline_keyboard_schedule
from time_func import get_day, position_of_schedule
from db_func import get_schedule_by_group
from sqlalchemy.orm import sessionmaker
from db import engine


Session = sessionmaker(bind=engine)
session = Session()
load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_schedule = telebot.types.KeyboardButton(text="Розклад",)
    button_info = telebot.types.KeyboardButton(text="Про нас")
    keyboard.add(button_schedule, button_info)
    bot.send_message(message.chat.id,  reply_markup=keyboard,
                     text="Вас вітає, телеграм бот ВСП Технічного фахового коледжу"
                     " Національного університету 'Львівська Політехніка'")


@bot.message_handler(commands=['schedule'])
def schedule(message):
    bot.send_message(message.chat.id, make_schedule(), reply_markup=create_inline_keyboard_schedule())


@bot.message_handler(commands=['info'])
def info(message):
    info_func(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    select_schedule = make_schedule(call.data)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                          text=select_schedule, reply_markup=create_inline_keyboard_schedule(int(call.data)))


@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    if message.text.lower() == 'про нас':
        info_func(message)
    if message.text.lower() == 'розклад':
        bot.send_message(message.chat.id, make_schedule(), reply_markup=create_inline_keyboard_schedule())


def info_func(message):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=3)
    url_button = telebot.types.InlineKeyboardButton(text="Посилання на наш сайт", url="http://www.techcol.lviv.ua/")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Інформація про коледж', reply_markup=keyboard)


def make_schedule(day=get_day(), group='41-КІ'):
    position = position_of_schedule()
    extra_point = 1
    if position % 2 == 2:
        extra_point = 2

    string = f'Група: {group}\n\n'
    schedules = get_schedule_by_group(session, group)
    for schedule in schedules:
        if (schedule.day_of_week == str(day) and
                (schedule.position_of_week == 0 or
                 schedule.position_of_week == extra_point or schedule.position_of_week == position)):

            string += (f'{schedule.number_of_pair} - {schedule.pair.name}\n{clock_emoji} '
                           f'{schedule.time_start} - {schedule.time_end}\n{book_emoji} {schedule.teacher.name} {schedule.type_of_pair} {schedule.audience}\n\n')

    return string
