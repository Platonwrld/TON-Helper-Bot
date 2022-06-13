import asyncio
import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
loop = asyncio.get_event_loop()

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=storage)
