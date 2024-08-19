from asyncio import run

from aiogram import Bot, Dispatcher, types

dp = Dispatcher()


async def echo(message: types.Message, bot: Bot):
    await message.copy_to(chat_id=message.chat.id)


async def start():
    dp.message.register(echo)
    bot = Bot('7376727264:AAEngzsdZHFn29pXCzAvi3KRT8viZhtpQM4')

    await dp.start_polling(bot)


run(start())
