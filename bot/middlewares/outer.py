import logging

from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User

logger = logging.getLogger(__name__)


# middleware for passing admin only
class IsAdminOuterMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        logger.debug(
            "Entering middleware %s, event`s type %s",
            __class__.__name__,  # type:ignore
            event.__class__.__name__,
            )
        
        user: User = data.get('event_from_user')  # type:ignore
        
        # we can do something while entering middleware
        print(user.id)

        if user.id != 828900493:
            print(f"User {user.id} have try to reach your bot")
            return None
        
        result = await handler(event, data)
        
        logger.debug(
            "Exiting middleware %s, event`s type %s",
            __class__.__name__,  # type:ignore
            event.__class__.__name__,
        )
        
        # we can do something while exiting middleware
        print(f"User ID has changed {user.id + 1}")
        
        return result
