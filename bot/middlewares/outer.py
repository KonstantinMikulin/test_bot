import logging

from typing import Any, Awaitable, Callable, Dict, cast

from aiogram import Bot, BaseMiddleware
from aiogram.types import TelegramObject, User, Chat, Message

from cachetools import TTLCache # type:ignore

from sqlalchemy.ext.asyncio import AsyncSession

from bot.db.requests import upsert_user

logger = logging.getLogger(__name__)


class TrackAllUsersMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()
        self.cache = TTLCache(
            maxsize=1000,
            ttl=60 * 60 * 6
        )
        
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        event = cast(Message, event)
        user_id = event.from_user.id # type:ignore
        
        # update user`s data if user not in cache
        if user_id not in self.cache:
            session: AsyncSession = data['session']
            await upsert_user(
                session=session,
                telegram_id=event.from_user.id,  # type:ignore
                first_name=event.from_user.first_name,  # type:ignore
                last_name=event.from_user.last_name,  # type:ignore
            )
            self.cache[user_id] = None
        
        return await handler(event, data)


class IsUserOuterMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        logger.debug(
            "Enter middleware %s, event`s type %s",
            __class__.__name__,  # type:ignore
            event.__class__.__name__,
        )
        # get chat object from event
        chat: Chat = event.message.chat # type:ignore
        # get user object from event
        user: User = data.get("event_from_user")  # type:ignore
        # get bot object from worflow_data
        bot: Bot = data.get("bot") # type:ignore

        # we can do something while entering middleware
        print(f"This user {user.id} try to use this bot")

        if user.id not in (828900493, 5903864970):
            # send message to not allowed user
            await bot.send_message(
                chat_id=chat.id,
                text='You are not welcome here'
            )
            # sending warning message to admin
            await bot.send_message(
                chat_id=828900493,
                text=f"User {user.first_name}, {user.id} try to reach your bot"
                )
            print(f"User {user.id} is not allowed to use this bot")
            return None

        # we can do something while exiting middleware
        print(f"This user {user.id} is allowed to use this bot")
        
        result = await handler(event, data)

        logger.debug(
            "Exit middleware %s, event`s type %s",
            __class__.__name__,  # type:ignore
            event.__class__.__name__,
        )

        return result


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
        print(f"Let`s check if this user {user.id} is admin")

        if user.id != 828900493:
            print(f"No. This user {user.id} is not admin")
            return None
        
        result = await handler(event, data)
        
        logger.debug(
            "Exiting middleware %s, event`s type %s",
            __class__.__name__,  # type:ignore
            event.__class__.__name__,
        )
        
        # we can do something while exiting middleware
        print(f"Yes. This user {user.id} is admin")
        
        return result
