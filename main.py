from aiogram import *
import logging
from io import BytesIO

from config import token
from stilization import *

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
btn_art1 = types.KeyboardButton(text='Выделить контур')
btn_art2 = types.KeyboardButton(text='Градация серого')
btn_art3 = types.KeyboardButton(text='Перевернуть изображение')
btn_art4 = types.KeyboardButton(text='')
btn_menu = types.InlineKeyboardButton(text='Меню бота 📔')
style_keyboard.add(btn_art1, btn_art2, btn_art3, btn_art4, btn_menu)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Здравствуй!\nЯ PhotoSet Бот!\nДавай сделаем вашу фотографию интересной", reply_markup=style_keyboard)
    #await message.answer("Выберите то действие, которое хотели бы провести с фотографией:")


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

from PIL import Image, ImageFilter

@dp.message_handler(content_types=["photo"])
async def get_photo(message):
    user_photofile = await bot.get_file(message.photo[-1].file_id)
    # await message.photo[-1].download(file_info.file_path.split('photos/')[1]) # ++
    #photo = pict_rotate()
    user_photo = Image.open('assets/menu.png')
    user_rotatephoto = user_photo.rotate(180)
    await message.answer('Развернули фото на 180 гр.', user_rotatephoto)
    await message.answer('Что вы хотите наложить на фотографию?', reply_markup=style_keyboard)


@dp.message_handler(content_types=["document"])
async def get_document_set_philter(message):
    await message.answer('Получил изображение. Идет оброботка....')


# Бот запускает цикл для бесконечной работы
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
