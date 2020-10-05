import logging

from aiogram import Bot, Dispatcher, executor, types

import replace as rp

API_TOKEN = 'TOKEN'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['qe'])
async def replaice(message: types.Message):
    try:
        if (message.reply_to_message.text != None) or (message.reply_to_message.text == "None"):
            lang = "eng"
            replace = rp.replace(lang, message.reply_to_message.text)
            if replace:
                text = "Наверное " + message.reply_to_message.from_user.full_name + " хотел(а) сказать: " + replace
                await message.answer(text)
            else: 
                await message.answer("Похоже, что вы спутали команды, попробуйте /ad")
        else:
            await message.answer("Пишите команду в ответ на текстовое сообщение")
    except AttributeError:
        await message.answer("Пишите команду в ответ на сообщение")
  
@dp.message_handler(commands=['ad'])
async def replaice(message: types.Message):
    try:
        if (message.reply_to_message.text != None) or (message.reply_to_message.text == "None"):
            lang = "rus"
            replace = rp.replace(lang, message.reply_to_message.text)
            if replace:
                text = "Наверное " + message.reply_to_message.from_user.full_name + " хотел(а) сказать: " + replace
                await message.answer(text)
            else: 
                await message.answer("Похоже, что вы спутали команды, попробуйте /qe")
        else:
            await message.answer("Пишите команду в ответ на текстовое сообщение")
    except AttributeError:
        await message.answer("Пишите команду в ответ на сообщение")
    	
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)