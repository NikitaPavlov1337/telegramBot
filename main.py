from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db

async def on_startup(_):
  print('Бот вышел в онлайн')
  sqlite_db.sql_start()

from handlers import client, other


client.register_handlers_client(dp)

other.register_handlers_other(dp)


# await message.reply(message.text)
# await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, on_startup=on_startup)
