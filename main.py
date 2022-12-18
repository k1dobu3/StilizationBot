from aiogram import *
import logging
import os

import stilization
from config import token
from stilization import *
# import weather
# import googlepict


logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher(bot)

# Menu buttons
menu_keyboard = types.ReplyKeyboardMarkup(row_width=1)
btn_nav1 = types.KeyboardButton(text='Продолжить работу 📸')
btn_nav2 = types.KeyboardButton(text='Поддержать проект 💸')
btn_nav3 = types.KeyboardButton(text='Разработчики 👥')
menu_keyboard.add(btn_nav1, btn_nav2, btn_nav3)

# Only Start buttons

start_keyboard = types.ReplyKeyboardMarkup(row_width=1)
start_keyboard.add(btn_nav1)

# Style buttons
style_keyboard = types.ReplyKeyboardMarkup(row_width=2)
btn_menu = types.InlineKeyboardButton(text='Меню бота 📔')
style_keyboard.add(btn_menu)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Здравствуй!\nЯ PhotoSet Бот!\nДавай сделаем вашу фотографию интересной\n\nОтправь фото с одной из цифр:\n1-перевернуть фото\n2-монохром\n3-оставить контуры",
        reply_markup=style_keyboard)


@dp.message_handler(commands=['menu'])
async def send_menubar(message: types.Message):
    await message.reply("Меню бота:", reply_markup=menu_keyboard)


# 4 Лаба по WEB
@dp.message_handler(commands=['help'])
async def send_helpmenu(message: types.Message):
    await message.answer(
        "Рабочие команды:\n\n/start - начало работы\n/menu - меню бота",
        reply_markup=start_keyboard)


# @dp.message_handler(commands=['weather'])
# async def get_localweather(message: types.Message):
#     ourcity_weather = weather.get_wether('Rostov-on-Don')
#     await message.reply(
#         f"Погода в выбранном городе: {ourcity_weather[0][0]}\n\nСостояние неба: {ourcity_weather[1]}\nТемпература: {ourcity_weather[2]}℃")
#
#
# @dp.message_handler(commands=['animals'])
# async def get_randomanimal(message: types.Message):
#     await message.answer(
#         f"Напиши:\n<b>Котик</b> для поисков котиков\n<b>Лисичк</b> для поисков лисичек\n<b>Енотик</b> для поисков енотов\n<b>Supra</b> для поисков кошечки, хе-хе",
#         parse_mode='html')


@dp.message_handler(content_types=["photo"])
async def get_photoandtext(message):
    file_info = await bot.get_file(message.photo[-1].file_id)
    user_decide = message.caption
    print(user_decide)
    photo_pathname = file_info.file_path.split('photos/')[1]
    await message.photo[-1].download(destination_file=photo_pathname)
    if user_decide == '1':
        fucn_answer = stilization.pict_rotate(photo_pathname)
        photo = open(f'{photo_pathname}', 'rb')
        if fucn_answer: await message.answer_photo(photo)
        os.remove(f"{photo_pathname}")
    elif user_decide == '2':
        fucn_answer = stilization.pict_mohohrom(photo_pathname)
        photo = open(f'{photo_pathname}', 'rb')
        if fucn_answer: await message.answer_photo(photo)
        os.remove(f"{photo_pathname}")
    elif user_decide == '3':
        fucn_answer = stilization.pict_contour(photo_pathname)
        photo = open(f'{photo_pathname}', 'rb')
        if fucn_answer: await message.answer_photo(photo)
        os.remove(f"{photo_pathname}")
    else:
        print("PASS")
    await message.answer('VOT')


@dp.message_handler(content_types=["document"])
async def get_document_set_philter(message):
    await message.answer('Получил изображение. Идет оброботка....')


@dp.message_handler(content_types="text")
async def echo(message: types.Message):
    if message.text == 'Разработчики 👥':
        url_keyboard = types.InlineKeyboardMarkup(row_width=1)
        btn_url1 = types.InlineKeyboardButton(text='GitHub', url='https://github.com/k1dobu3/StilizationBot')
        url_keyboard.add(btn_url1)
        await message.reply(
            'Разработчики:\n<b>Гордиенко Кирилл</b>\n<b>Крылосов Игорь</b>\n<b>Пятаков Дмитрий</b>\n\nНаш проект на платформах:',
            reply_markup=url_keyboard, parse_mode='html')
    elif message.text == 'Меню бота 📔':
        await message.answer("Меню бота:", reply_markup=menu_keyboard)
    elif message.text == 'Продолжить работу 📸':
        await message.reply("Отправь фото с одной из цифр:\n1-перевернуть фото\n2-монохром\n3-стиль Ван Гога(контуры)", reply_markup=style_keyboard)
    elif message.text == 'Поддержать проект 💸':
        await message.answer("Потом тут будет поддержка нашего проекта, а пока назад в меню",
                             reply_markup=style_keyboard)
    # elif message.text == 'Котик' or 'Лисичк' or 'Енотик' or 'Supra':
    #     await message.answer(f"Вот ваш {message.text}:")
    #     await message.answer("PLS ONE SECOND")
    #     google_answer1 = googlepict.get_googlepicturl(message.text)
    #     google_answer2 = googlepict.get_googlepicturl(message.text)
    #     google_answer3 = googlepict.get_googlepicturl(message.text)
    #     media = types.MediaGroup()
    #     media.attach_photo(f'{google_answer1}')
    #     print(1)
    #     media.attach_photo(f'{google_answer2}')
    #     media.attach_photo(f'{google_answer3}')
    #     await bot.send_media_group(message.chat.id, media=media)
    else:
        await message.answer(message.text)


# Бот запускает цикл для бесконечной работы
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
