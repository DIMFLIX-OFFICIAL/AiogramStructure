import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy.orm import sessionmaker

from General import config as cfg
from General.database.utils import create_db_session
from General.database.database import DB


db_session: sessionmaker = asyncio.run(create_db_session())
db = DB(db_session)
bot: Bot = Bot(token=cfg.BOT_TOKEN, parse_mode="HTML")
dp: Dispatcher = Dispatcher(storage=MemoryStorage())


