import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

from bot.config_reader import get_config, BotConfig, DbConfig
from bot.handlers import get_commands_routers, admin_router
from bot.handlers.main_menu import set_main_menu
from bot.middlewares import IsUserOuterMiddleware, SomeInnerMiddleware, ChatActionInnerMiddleware
from bot.db.tables import metadata

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
        # simple text quenue
        await conn.execute(text("SELECT 1"))
    
    # create table
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
    
    # creating dispatcher object
    dp = Dispatcher(admin_id=bot_config.admin_id, db_engine=engine)
    # creating bot object
    bot = Bot(
        token=bot_config.token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )
    
    # passing bot object to workflow data
    dp.workflow_data.update({'bot': bot, 'my_dp': dp})
    
    # connecting handlers`routers
    dp.include_routers(*get_commands_routers())
    
    # registering middlewares
    dp.update.outer_middleware(IsUserOuterMiddleware())
    admin_router.message.middleware(SomeInnerMiddleware())
    admin_router.message.middleware(ChatActionInnerMiddleware())
    
    # set main menu
    await set_main_menu(bot)
    
    # skip updates and run pulling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    
asyncio.run(main())
