from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext

from config import TOKEN

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot,
                storage=storage)


class ProfileStatesGroup(StatesGroup):
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
    await ProfileStatesGroup.photo.set() # установили для бота состояние "фото"


@dp.message_handler(content_types=['photo'], state=ProfileStatesGroup.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

    await message.reply('Now send your name')
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await message.reply('How old are you?')
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.age)
async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text

    await message.reply('Write description')
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
        await bot.send_photo(chat_id=message.chat.id,
                             photo=data['photo'],
                             caption=f"{data['name']}, {data['age']}\n{data['description']}")

    await message.reply('All data was loaded')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
