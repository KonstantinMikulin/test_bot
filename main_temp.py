from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
storage = MemoryStorage()


class ProfileStatesGroup(StatesGroup)
    photo = State()
    name = State()
    age = State()
    description = State()



async def on_startup(_):
    print('Bot is running')


def get_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('/create'))

    return kb


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer(text='Hello! Send "/create"',
                         reply_markup=get_kb())


@dp.message_handler(commands='create')
async def cmd_create(message: types.Message):
    await message.reply('Let`s start! Send me your photo')
    await ProfileStatesGroup.photo.set()


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
