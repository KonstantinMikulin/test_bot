import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from bot.config_reader import get_config, BotConfig, DbConfig
from bot.handlers import get_commands_routers
from bot.handlers.main_menu import set_main_menu
from bot.db import Base
from bot.middlewares import (
    DbSessionMiddleware,
    TrackAllUsersMiddleware
    )


async def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s] #%(levelname)-8s %(filename)s:"
        "%(lineno)d - %(name)s - %(message)s",
    )

    logger = logging.getLogger(__name__)
    logger.info('Bot starts')
    
    # creating bot`s config 'object'
    bot_config = get_config(BotConfig, 'bot')
    
    # create database config 'object'
    db_config = get_config(DbConfig, "db")
    
    # create sqlachemy engine
    engine = create_async_engine(
        url=str(db_config.dsn),
        echo=db_config.is_echo
    )
    
    # open new connection with database
    async with engine.begin() as conn:
        # simple text query
        await conn.execute(text("SELECT 1"))
    
    # create tables
    async with engine.begin() as connection:
        # await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
    
    # Инициализируем хранилище (создаем экземпляр класса MemoryStorage)
    storage = MemoryStorage()
    
    # Создаем "базу данных" пользователей
    user_dict: dict[int, dict[str, str | int | bool]] = {} # type:ignore
    
    # creating dispatcher object
    dp = Dispatcher(admin_id=bot_config.admin_id, db_engine=engine, storage=storage)
    
    # creating bot object
    bot = Bot(
        token=bot_config.token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )
    
    # passing bot object to workflow data
    dp.workflow_data.update({'bot': bot, 'my_dp': dp, 'user_dict': user_dict})
    
    # registering middlewares
    Sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
    dp.update.outer_middleware(DbSessionMiddleware(Sessionmaker))
    dp.message.outer_middleware(TrackAllUsersMiddleware())
    
    # connecting handlers`routers
    dp.include_routers(*get_commands_routers())
    
    # set main menu
    await set_main_menu(bot)
    
    # skip updates and run pulling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    
asyncio.run(main())
