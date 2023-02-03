#TODO: сделать бот, который отправляет одну фотогорафию с инлайн клавиатурой
from aiogram import Bot, Dispatcher, executor, types
import config

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)

is_voted = False


async def on_startup(_):
    print('Bot is running!')


@dp.message_handler(commands='photo')
async def cmd_start(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMzmn84CZqMM3f1jK009KsRRf_W8q5vF0q-g&usqp=CAU',
                         caption='Do you like it?',
                         reply_markup=config.inline_keyboard)
    await message.delete()


@dp.callback_query_handler(text='remove all')
async def remove_cb_data(callback: types.CallbackQuery):
    await callback.message.delete()


@dp.callback_query_handler()
async def photo_callback(callback:  types.CallbackQuery):
    global is_voted

    if not is_voted:
        if callback.data == 'like':
            await callback.answer(text='You like it!')
            is_voted = True
        await callback.answer(text='You dont like it :(')
        is_voted = True
    await callback.answer(text='You voted ALREDY!',
                          show_alert=True)


    if callback.data == 'like':
        if not is_voted:
            await callback.answer(text='You like it!')
            is_voted = not is_voted
        else:
            await callback.answer(text='You voted already!')
    elif callback.data == 'dislike':
        if not is_voted:
            await callback.answer(text='You dont like it :(')
            is_voted = not is_voted
        else:
            await callback.answer(text='You voted ALREADY!')




if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)



#TODO: у клавиатуры будет три опции: 1. Убрать клавиатуру и фото.
