from aiogram import Bot, Dispatcher, executor, types
import config

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot is running')


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         caption='Like it?',
                         photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMzmn84CZqMM3f1jK009KsRRf_W8q5vF0q-g&usqp=CAU',
                         reply_markup=config.inline_keyboard)


@dp.callback_query_handler()
async def ikb_callback_handler(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer(text='You like it!')
    else:
        await callback.answer(text='You don`t like it')


if __name__ == '__main__':
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)
