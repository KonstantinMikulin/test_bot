import asyncio
import logging

from aiogram import Dispatcher, Bot

from bot.config_reader import get_config, BotConfig
from bot.handlers import get_routers


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
    # creatin bot object
    bot = Bot(token=bot_config.token.get_secret_value())
    
    # connecting handlers`routers
    dp.include_routers(*get_routers())
    
    await dp.start_polling(bot)
    
    
asyncio.run(main())
