import logging

from aiogram.filters import BaseFilter
from aiogram.types import TelegramObject, User

logger = logging.getLogger(__name__)


# filter for admin
class IsAdminFilter(BaseFilter):
    async def __call__(
        self,
        event: TelegramObject
    ) -> bool:
        logger.debug('Entering filter %s', __class__.__name__) # type:ignore
        
        user: User = event.from_user # type:ignore

        # check if user id in admin`s list
        if user.id == 828900493:
            logger.debug('Exit filter %s', __class__.__name__)  # type:ignore

            return True
        
        return False
