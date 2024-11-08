from sqlalchemy.dialects.postgresql import insert as upsert
from sqlalchemy.ext.asyncio import AsyncSession

from bot.db.models import User, Weight, MeasureBicep, MeasureHips, MeasureWaist


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


# request to add user weight to db
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


# request to add tail measurement to db
async def add_waist(
    session: AsyncSession,
    telegram_id: int,
    waist: int
    ):
    """
    Добавление записи объема талии пользователя
    :param session: сессия СУБД
    :param telegram_id: айди пользователя
    :param waist: объем талии пользователя
    """

    new_waist = MeasureWaist(user_id=telegram_id, waist=waist)
    session.add(new_waist)
    await session.commit()


# request to add hips measurement to db
async def add_hips(session: AsyncSession, telegram_id: int, hips: int):
    """
    Добавление записи объема пользователя
    :param session: сессия СУБД
    :param telegram_id: айди пользователя
    :param hips: объем талии пользователя
    """

    new_hips = MeasureHips(user_id=telegram_id, hips=hips)
    session.add(new_hips)
    await session.commit()


# request to add bicep measurement to db
async def add_bicep(session: AsyncSession, telegram_id: int, bicep: int):
    """
    Добавление записи объема пользователя
    :param session: сессия СУБД
    :param telegram_id: айди пользователя
    :param bicep: объем талии пользователя
    """

    new_bicep = MeasureBicep(user_id=telegram_id, bicep=bicep)
    session.add(new_bicep)
    await session.commit()
