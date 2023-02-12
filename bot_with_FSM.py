from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext

from config import TOKEN
from sqlite import db_start, create_profile, edit_profile

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
    await db_start()


# Keyboard for starting profiling
def get_create_kb():
    kb_1 = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_1.add(KeyboardButton('/create'))

    return kb_1


# Keyboard for canceling profiling
def get_cancel_kb():
    kb_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_2.add(KeyboardButton('/cancel'))

    return kb_2


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer(text='Hello! Send "/create"',
                         reply_markup=get_create_kb())

    await create_profile(user_id=message.from_user.id)


# Command for cancelling  profiling process.
@dp.message_handler(commands='cancel', state='*')  # Need to mention that bot can be in any state
async def cmd_cancel(message: types.Message, state: FSMContext):
    if state is None:
        return

    await state.finish()
    await message.answer(text='Profiling was stopped',
                         reply_markup=get_create_kb())


# Старт сбора данных. Запрос на отправку фото.
@dp.message_handler(commands='create')
async def cmd_create(message: types.Message):
    await message.reply(text='Let`s start! Send me your photo',
                        reply_markup=get_cancel_kb())
    await ProfileStatesGroup.photo.set()  # установили для бота состояние "фото"


# Проверка того, что пользователь прислал фото.
@dp.message_handler(lambda message: not message.photo,
                    state=ProfileStatesGroup.photo)  # We need 'state' argument. Only if bot in this state, this handler will work.
async def check_photo(message: types.Message):
    await message.reply('This is not photo')


# State set as 'photo'. Request fot name from user.
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


# Check for correct age
@dp.message_handler(lambda message: not message.text.isdigit() or int(message.text) > 100,
                    state=ProfileStatesGroup.age)
async def check_photo(message: types.Message):
    await message.reply('Input correct age')


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

    await edit_profile(state, user_id=message.from_user.id)
    await message.reply('All data was loaded')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
