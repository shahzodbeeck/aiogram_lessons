from aiogram import Bot
from aiogram.types import Message


async def user_info(message: Message, bot: Bot):
    user = await bot.get_chat(message.from_user.id)
    photos = await message.from_user.get_profile_photos()
    text = (f'{message.from_user.mention_html("User info:")}\n\n'
            f'Ism familiya : {user.full_name}\n\n'
            f''f'ID : {user.id}\n\n')
    if user.bio: text += f"User bio: {user.bio}\n\n"
    if user.username: text += f"User username: @{user.username}\n\n"
    if photos.photos:
        await message.answer_photo(photos.photos[0][-1].file_id, caption=text,parse_mode="HTML")
    else:
        await message.answer(text,parse_mode='HTML')
