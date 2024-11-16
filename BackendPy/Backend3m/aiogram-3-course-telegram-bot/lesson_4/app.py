import asyncio,logging
import os

logging.basicConfig(level=logging.INFO)

from aiogram import Bot, Dispatcher, types


from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from handlers.user_private import user_private_router
from handlers.user_group import user_group_router
from common.bot_cmds_list import private

ALLOWED_UPDATES = ['message, edited_message']

# bot = Bot(token=os.getenv('7334474558:AAGVgIwk6a9VGzhbBULya4n1SRqYzwXX2YU'))
bot=Bot(token='7301331561:AAH4j0tWAo0T0JxsAx4-b-sVwLfV2KoGv9o')
dp = Dispatcher()

dp.include_router(user_private_router)
dp.include_router(user_group_router)



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())