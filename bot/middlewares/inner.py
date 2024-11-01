import logging

from typing import Callable, Awaitable, Any, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

logger = logging.getLogger(__name__)


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
