import asyncio
import logging

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from sqlalchemy import delete, select, column
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio.engine import AsyncEngine

logger = logging.getLogger(__name__)

# creating router`s onject
admin_router = Router(name="admin router")


# /start command add data about user into db
@admin_router.message(CommandStart())
async def cmd_admin_start(message: Message, db_engine: AsyncEngine):
    logger.info("Enter admin`s /start handler")
    
    stmt = insert(users_table).values(
        telegram_id=message.from_user.id,  # type:ignore
        first_name=message.from_user.first_name,  # type:ignore
        last_name=message.from_user.last_name,  # type:ignore
    )
    
    do_ignore = stmt.on_conflict_do_nothing(index_elements=["telegram_id"])
    
    async with db_engine.connect() as conn:
        await conn.execute(do_ignore)
        await conn.commit()
    
    await message.answer('<b>Admin</b>, you sent /start! Welcome!')
    
    logger.info("Exit admin`s /start handler")
    

@admin_router.message(Command(commands="deleteme"))
async def cmd_delteme(message: Message, db_engine: AsyncEngine):
    stmt = (delete(users_table).where(users_table.c.telegram_id == message.from_user.id)) # type:ignore
    
    async with db_engine.connect() as conn:
        await conn.execute(stmt)
        await conn.commit()
    
    await message.answer("Your data was delete")


# command /test 'only' for admin
@admin_router.message(
    Command(commands="stats"),
    flags={"long_operation": "typing"}
)
async def cmd_test(message: Message):
    await asyncio.sleep(3)
    await message.answer('Here is statistics, admin!')
