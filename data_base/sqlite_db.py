import sqlite3 as sq


def sql_start():
  global base, cur
  base = sq.connect('residence.db')
  cur = base.cursor()
  if base:
    print('Data base connected OK!')
  base.execute('CREATE TABLE IF NOT EXISTS housemates(contract TEXT, contact TEXT, building TEXT, section TEXT, floor TEXT, flat TEXT)')
  base.commit()


async def sql_add_command(state):
  async with state.proxy() as data:
    try:
      cur.execute('INSERT INTO housemates VALUES (?, ?, ?, ?, ?, ?)', tuple(data.values()))
      base.commit()
    except ValueError:
      cur.execute('INSERT INTO housemates VALUES (?, ?, ?, ?, ?, ?)', (0, 0, 0, 0, 0, 0,))
      print(ValueError)