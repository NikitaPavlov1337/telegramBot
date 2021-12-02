from create_bot import bot, dp
from keyboards import kb_client
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from data_base import sqlite_db

# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
  try:
    await bot.send_message(message.from_user.id, 'Добрый день, вы проходите верификацию, ответьте на все вопросы', reply_markup=kb_client)
    await message.delete()
  except ValueError:
    await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/CheckTheResident_bot')

class FSMAUser(StatesGroup):
  contract = State()
  building = State()
  section = State()
  floor = State()
  flat = State()

#начало диалога загрузки нового пункта меню
# @dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message: types.Message):
  await FSMAUser.contract.set()
  await message.reply('Напишите номер ДДУ...')


#ловим первый ответ  пишем в словарь
# @dp.message_handler(content_types=['photo'], state=FSMAUser.photo)
async def load_contract(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['contract'] = message.text
    username = message.from_user.username
    if not username:
      data['nameSurname'] = message.from_user.full_name
    data['username'] = username
  await FSMAUser.next()
  await message.reply('Теперь введите номер корпуса...')


#ловим второй ответ
# @dp.message_handler(state=FSMAUser.name)
async def load_building(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['building'] = message.text
  await FSMAUser.next()
  await message.reply('Теперь введите номер секции...')


#ловим третий ответ
# @dp.message_handler(state=FSMAUser.description)
async def load_section(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['section'] = message.text
  await FSMAUser.next()
  await message.reply('Укажите этаж...')


#ловим последний ответ и используем полученные данные
# @dp.message_handler(state=FSMAUser.price)
async def load_floor(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['floor'] = message.text
  await FSMAUser.next()
  await message.reply('Укажите номер квартиры...')


#ловим последний ответ и используем полученные данные
# @dp.message_handler(state=FSMAUser.price)
async def load_flat(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['flat'] = message.text
  await sqlite_db.sql_add_command(state)
  await message.reply('Спасибо, Ваши данные сохранены')
  await state.finish() #команда все очищает, все данные



# Выход из сотояний
@dp.message_handler(state="*", commands='отмена')
@dp.message_handler(Text(equals='отмена', ignore_case = True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
  current_state = await state.get_state()
  if current_state is None:
    return
  await state.finish()
  await message.reply('Верификация прервана пользователем')


def register_handlers_client(dp: Dispatcher):
  dp.register_message_handler(commands_start, commands=['start', 'Help'])
  dp.register_message_handler(cancel_handler, state='*', commands=['Отмена'])
  dp.register_message_handler(cancel_handler, Text(equals='/Отмена', ignore_case=True), state='*')
  dp.register_message_handler(cm_start, commands=['Начать'], state=None)
  dp.register_message_handler(load_contract,state=FSMAUser.contract)
  dp.register_message_handler(load_building, state=FSMAUser.building)
  dp.register_message_handler(load_section, state=FSMAUser.section)
  dp.register_message_handler(load_floor, state=FSMAUser.floor)
  dp.register_message_handler(load_flat, state=FSMAUser.flat)















