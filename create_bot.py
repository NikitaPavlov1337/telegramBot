from aiogram import Bot
from aiogram.dispatcher import Dispatcher
# from config import token
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = os.getenv('tgmb')
storage = MemoryStorage()

bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)
