import telebot
from data import left_arrow_unicode
from time_func import get_day


def create_inline_keyboard_schedule(day=get_day()):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=5)
    mon_button = telebot.types.InlineKeyboardButton(text="ПН", callback_data="1")
    tue_button = telebot.types.InlineKeyboardButton(text="ВТ", callback_data="2")
    wed_button = telebot.types.InlineKeyboardButton(text="СР", callback_data="3")
    thu_button = telebot.types.InlineKeyboardButton(text="ЧТ", callback_data="4")
    fri_button = telebot.types.InlineKeyboardButton(text="ПТ", callback_data="5")

    if day == 1:
        mon_button.text += left_arrow_unicode
    elif day == 2:
        tue_button.text += left_arrow_unicode
    elif day == 3:
        wed_button.text += left_arrow_unicode
    elif day == 4:
        thu_button.text += left_arrow_unicode
    elif day == 5:
        fri_button.text += left_arrow_unicode

    keyboard.add(mon_button, tue_button, wed_button, thu_button, fri_button)

    return keyboard
