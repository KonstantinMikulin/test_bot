from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from config import TOKEN

storage = MemoryStorage()
bot = Bot(TOKEN)
dp = Dispatcher(bot,
                storage=storage)


def get_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Start work'))

    return kb


def get_cancel_kb():
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/cancel'))


class ClientStatesGroup(StatesGroup):
    photo = State()
    description = State()


async def on_startup(_):
    print('Bot is running')


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer(text='Hello!',
                         reply_markup=get_keyboard())


@dp.message_handler(commands='cancel', state='*')
async def cmd_start(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await message.reply(text='Cancelled',
                        reply_markup=get_keyboard())
    await state.finish()


@dp.message_handler(Text(equals='Start work', ignore_case=True), state=None)
async def start_work(message: types.Message):
    await ClientStatesGroup.photo.set()
    await message.answer(text='Send photo first please',
                         reply_markup=get_cancel_kb())


@dp.message_handler(lambda message: not message.photo, state=ClientStatesGroup.photo)
async def check_photo(message: types.Message):
    return await message.reply(text='This is NOT photo')


@dp.message_handler(lambda message: message.photo, content_types=['photo'], state=ClientStatesGroup.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

    await ClientStatesGroup.next()
    await message.reply(text='Now send description please')


@dp.message_handler(state=ClientStatesGroup.description)
async def load_desc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text

    await message.reply(text='Your photo was saved')

    async with state.proxy() as data:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=data['photo'],
                             caption=data['description'])

    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
