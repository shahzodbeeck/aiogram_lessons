from asyncio import run

from aiogram import Bot, Dispatcher, types

dp = Dispatcher()


async def start_answer(bot: Bot):
    await bot.send_message(chat_id='1948897525', text='Bot ishga tushdi✅')


async def shutdown_answer(bot: Bot):
    await bot.send_message(chat_id='1948897525', text='Bot ochirildi ❌')


async def echo(message: types.Message, bot: Bot):
    await message.copy_to(chat_id=message.chat.id)


async def start():
    dp.startup.register(start_answer)
    dp.message.register(echo)
    dp.shutdown.register(shutdown_answer)
    bot = Bot('7376727264:AAEngzsdZHFn29pXCzAvi3KRT8viZhtpQM4')

    await dp.start_polling(bot)


run(start())
