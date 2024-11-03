import logging

from typing import Callable, Awaitable, Any, Dict

from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject
from aiogram.dispatcher.flags import get_flag
from aiogram.utils.chat_action import ChatActionSender

logger = logging.getLogger(__name__)


# inner middleware with dependency injection of 'some_new'
class SomeInnerMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        logger.debug(
            'Enter middleware %s, event type %s',
            __class__.__name__, # type:ignore
            event.__class__.__name__
        )
        data['some_new'] = 'New info'
        
        result = await handler(event, data)
        
        logger.debug('Exit middleware %s', __class__.__name__)  # type:ignore

        return result


class ChatActionInnerMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        long_operation_type = get_flag(data, "long_operation")
        bot: Bot = data.get('bot') # type:ignore
        
        # if there is no this flag in handler
        if not long_operation_type:
            return await handler(event, data)
        
        # if there is flag
        async with ChatActionSender(
            action=long_operation_type,
            bot=bot,
            chat_id=event.chat.id # type:ignore
        ):
            return await handler(event, data)
