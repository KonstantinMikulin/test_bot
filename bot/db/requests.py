from typing import cast

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert as upsert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload

from bot.db.models import User, Weight


async def upsert_user(
    session: AsyncSession,
    telegram_id: int,
    first_name: str,
    last_name: str | None = None
):
    """
    Добавление или обновление пользователя
    в таблице users
    :param session: сессия СУБД
    :param telegram_id: айди пользователя
    :param first_name: имя пользователя
    :param last_name: фамилия пользователя
    """
    
    stmt = upsert(User).values(
        {
            "telegram_id": telegram_id,
            "first_name": first_name,
            "last_name": last_name
        }
    )
    
    stmt = stmt.on_conflict_do_update(
        index_elements=["telegram_id"],
        set_=dict(
            first_name=first_name,
            last_name=last_name
        )
    )

    await session.execute(stmt)
    await session.commit()


async def add_weight(
    session: AsyncSession,
    telegram_id: int,
    weight: int
):
    """
    Добавление записи веса пользователя
    :param session: сессия СУБД
    :param telegram_id: айди пользователя
    :param weight: вес пользователя
    """
    
    new_weight = Weight(
        user_id=telegram_id,
        weight=weight
    )
    session.add(new_weight)
    await session.commit()