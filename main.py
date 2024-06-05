import asyncio
import os
import re
from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message,
    Document
    # KeyboardButton,
    # ReplyKeyboardMarkup,
    # CallbackQuery,
)
from PIL import Image
from aiogram.filters import CommandStart
from admin import TOKEN
from contrast import imgCorrect
from ocr_img import ocr_my_img, split_image
from text import cards
bot = Bot(TOKEN)
dp = Dispatcher()





@dp.message(CommandStart())
async def cmd_started(message: Message):
    # keyboard = ReplyKeyboardMarkup(
    #     keyboard=[
    #         [KeyboardButton(text="Начать")],
    #     ]
    # )
    await message.answer("🇬🇧 Welcome to Hamster Upgrade! If you want to get a list for profitable upgrade cards. Send a screenshot\n*************************\n- The screenshot must be sent without compression as a file\n- The supported formats are jpg and png")
    await message.answer("🇷🇺 Добро пожаловать в Hamster Upgrade! Если вы хотите получить список для выгодного апгрейда своих карт. Отправьте скриншот\n*************************\n- Скриншот нужно отправлять без сжатия в виде файла\n- Поддерживаются форматы jpg и png")



# @dp.message(F.text == "Начать")
# async def cmd_start(message: Message):
#     if f"{message.from_user}" != ID:
#         await message.answer("Дождитесь ответа, вам ответят в порядке очереди.")
#         if connect == "":
#             await bot.send_message(ID, "Новый клиент!")
#             await bot.send_photo(ID, value)


    


# @dp.callback_query()
# async def process_callback(callback_query: CallbackQuery):
#     print(f"callback query: {callback_query.data}")
#     global client_data, connect
#     await bot.send_message(ID, f"✅ Подключение к чату: {callback_query.data}")
#     connect = f"{callback_query.data}"
#     for value in client_data[callback_query.data]:
#         if value[:1:] == "|":
#             await bot.send_message(ID, value)
#         else:
#             await bot.send_photo(ID, value)


# @dp.message(F.text)
# async def cmd_problem(message: Message):
#         print(message.text.split())


# @dp.message(F.text == "Контакты")
# async def cmd_contact(message: Message):
#     await message.answer(contact_text)


# @dp.message(F.text == "Наш адрес")
# async def cmd_address(message: Message):
#     await message.answer(address)

@dp.message(F.document)
async def photo_handler(message: Message):
    file_format = message.document.mime_type.split("/")[-1]

    await message.answer("Loading...\Загрузка...");
    file_id = message.document.file_id
    file = await bot.get_file(file_id) 
    filename= f'{message.from_user.id}.{file_format}' 
    await bot.download_file(file.file_path, destination=filename)
    imgCorrect(filename)
    left_file,right_file = split_image(filename)
    left_text = ocr_my_img(left_file)
    # right_text = ocr_my_img(right_file)
    # print(left_text.split())
    algo_decoded(left_text.split())
    print('\n\n')
    # right_text = ocr_my_img(right_file)
    # print(right_text)

# Пример использования
    # split_image('your_image.png')

    # await message.answer(text);
    if os.path.isfile(filename): 
        os.remove(filename) 
        print("success") 
    else:
        print("File doesn't exists!")






def algo_decoded(text):
   localCards=cards
   delsymbols = ['@', '€','tokens','hour','per','pairs','Profit']
   text = [i for i in text if i not in delsymbols]
   print(text)
   
   counters = [0 for _ in range(len(localCards))]
   profit_and_price = []
    # \d+ соответствует одной или более цифрам, K - это буква "K"
   print('\n\n')
   for i in range(len(text)):
       if (len(text[i])>1):
          if (re.search(r'\d+[KM]$', text[i],re.IGNORECASE)):
              text[i]=text[i].lower()
              if ('k' in text[i]):
                  text[i]=text[i].replace('k','')
                  if (text[i].isdigit()):
                      profit_and_price.append(float(text[i])*1000)
                  else:
                      profit_and_price.append(text[i]+'no')
              elif ('m' in text[i]):
                  text[i]=text[i].replace('m','')
                  if (text[i].isdigit()):
                      profit_and_price.append(float(text[i])*1000000)
                  else:
                      profit_and_price.append(text[i]+'no')
       for j in range(len(localCards)):
          for k in range(len(localCards[j])):
              if (text[i] in localCards[j][k]):
                  print(localCards[j][k])
                  counters[j] +=1
                #   j[k]= "✅"+j[k]
   print(counters)
   print(counters.index(max(counters)))
#    for i in range(len(localCards[counters.index(max(counters))])):                
        
# @dp.message(F.text)
# async def saver(message: Message):
#     print("texteeeed")
#     global connect
#     if f"{message.from_user.id}" != ID and connect != f"{message.from_user.id}":
#         if (
#             message.text != "Отправил"
#             and message.text != "У меня проблема"
#             and message.text != "Контакты"
#             and message.text != "Наш адрес"
#         ):
#             adder(f"{message.from_user.id}", message.text)
#     elif connect == f"{message.from_user.id}":
#         await bot.send_message(ID, message.text)
#     elif f"{message.from_user.id}" == ID and connect != "":
#         if message.text == ".":
#             await bot.send_message(ID, f"⛔️ Отключение чата с: {connect}")
#             client_data.pop(connect)
#             await bot.send_message(ID, f"⛔️ Удален чат с: {connect}")
#             connect = ""
#         else:
#             await bot.send_message(connect, message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())