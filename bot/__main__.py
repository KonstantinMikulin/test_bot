import asyncio
import logging

from aiogram import Dispatcher, Bot

from bot.config_reader import get_config, BotConfig
from bot.handlers import get_commands_routers
from bot.handlers.main_menu import set_main_menu

from bot.middlewares import IsAdminOuterMiddleware


async def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s] #%(levelname)-8s %(filename)s:"
        "%(lineno)d - %(name)s - %(message)s",
    )

    logger = logging.getLogger(__name__)
    logger.info('Bot starts')
    
    # creating config 'object'
    bot_config = get_config(BotConfig, 'bot')
    
    # creating dispatcher object
    dp = Dispatcher(admin_id=bot_config.admin_id)
    # creating bot object
    bot = Bot(token=bot_config.token.get_secret_value())
    
    # connecting handlers`routers
    dp.include_routers(*get_commands_routers())
    
    # registering middleware
    dp.update.outer_middleware(IsAdminOuterMiddleware())
    
    # set main menu
    await set_main_menu(bot)
    
    # skip updates and run pulling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    
asyncio.run(main())
