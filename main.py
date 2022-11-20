from aiogram import *
import logging

from config import token

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher(bot)

# Menu buttons
menu_keyboard = types.ReplyKeyboardMarkup(row_width=1)
btn_nav1 = types.KeyboardButton(text='Продолжить работу 📸')
btn_nav2 = types.KeyboardButton(text='Поддержать проект 💸')
btn_nav3 = types.KeyboardButton(text='Разработчики 👥')
menu_keyboard.add(btn_nav1, btn_nav2, btn_nav3)

# Style buttons
style_keyboard = types.ReplyKeyboardMarkup(row_width=2)
btn_art1 = types.KeyboardButton(text='Кандинский')
btn_art2 = types.KeyboardButton(text='Монет')
btn_art3 = types.KeyboardButton(text='Ван-Гог')
btn_art4 = types.KeyboardButton(text='Персонаж Дисней')
btn_menu = types.InlineKeyboardButton(text='Меню бота 📔')
style_keyboard.add(btn_art1, btn_art2, btn_art3, btn_art4, btn_menu)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Здравствуй!\nЯ PhotoSet Бот!\nДавай сделаем вашу фотографию интересной")
    await message.answer("Выберите стиль писателя под который вы хотели бы изменить свою фотографию:", reply_markup=style_keyboard)


@dp.message_handler(commands=['menu'])
async def send_menubar(message: types.Message):
    await message.reply("Меню бота:", reply_markup=menu_keyboard)


@dp.message_handler(content_types="text")
async def echo(message: types.Message):
    if message.text == 'Разработчики 👥':
        url_keyboard = types.InlineKeyboardMarkup(row_width=1)
        btn_url1 = types.InlineKeyboardButton(text='GitHub', url='https://github.com/k1dobu3')
        url_keyboard.add(btn_url1)
        await message.reply('Разработчики:\n<b>Гордиенко Кирилл</b>\n<b>Крылосов Игорь</b>\n<b>Пятаков Дмитрий</b>\n\nНаш проект на платформах:', reply_markup=url_keyboard, parse_mode='html')
    elif message.text == 'Меню бота 📔':
        await message.answer("Меню бота:", reply_markup=menu_keyboard)
    elif message.text == 'Продолжить работу 📸':
        await message.answer("Выберите стиль писателя под который вы хотели бы изменить свою фотографию:",
                             reply_markup=style_keyboard)
    elif message.text == 'Поддержать проект 💸':
        await message.answer("Потом тут будет поддержка нашего проекта, а пока назад в меню", reply_markup=style_keyboard)
    else:
        await message.answer(message.text)

# Бот запускает цикл для бесконечной работы
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
