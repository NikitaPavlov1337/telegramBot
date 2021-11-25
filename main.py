import logging
from aiogram.utils.executor import start_webhook
from create_bot import dp, bot
from data_base import sqlite_db
from heroku import WEBHOOK_URL, WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_URL_PATH


logging.basicConfig(level=logging.INFO)


from handlers import client, other


client.register_handlers_client(dp)
other.register_handlers_other(dp)


async def on_startup(dp):
  await bot.set_webhook(WEBHOOK_URL)
  sqlite_db.sql_start()
  print('Бот в сети')
# insert code here to run it after start

async def on_shutdown(dp):
  logging.warning('Shutting down..')
    # insert code here to run it before shutdown
    # Remove webhook (not acceptable in some cases)
  await bot.delete_webhook()

    # Close DB connection (if used)
  await dp.storage.close()
  await dp.storage.wait_closed()

  logging.warning('Bye!')


if __name__ == '__main__':
  start_webhook(
    dispatcher=dp,
    webhook_path=WEBHOOK_URL_PATH,
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates=False,
    host=WEBAPP_HOST,
    port=WEBAPP_PORT,)



