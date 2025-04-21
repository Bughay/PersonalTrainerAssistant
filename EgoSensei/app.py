from functions.models import *
from functions.bot_msg import *
from functions.personaltrainer import *
from functions.sql_update import *

import asyncio
import logging
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from langchain_core.prompts import ChatPromptTemplate

TOKEN =  '8159843803:AAF2hFbpOlbdzIPNmnVoYHiyZiWr9udhFjo'

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Hello {html.bold(message.from_user.full_name)}! Send me your diet, workout, or cardio log.")


@dp.message()
async def handle_message(message: Message):
    try:
        raw_data, category = personal_trainer_log(message.text)
        for i in range(len(raw_data)):
            if category == 'diet':
                update_food(raw_data[i])

            if category == 'training':
                update_exercise(raw_data[i])
            if category == 'cardio':
                update_cardio(raw_data[i])
                    
        formatted_response = format_response(raw_data,category)
        await message.answer(formatted_response)
    except Exception as e:
    
        logging.error(f"Error: {e}")
        await message.answer("⚠️ Error processing your message")
        

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())