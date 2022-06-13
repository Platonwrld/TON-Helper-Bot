from create_bot import dp, bot
from aiogram import Dispatcher, types
from aiogram.types import ContentType


async def send_photo_1(message : types.Message):

    await message.reply(message.photo[-1].file_id)


def media_register_handlers(dp: Dispatcher):

    dp.register_message_handler(send_photo_1, content_types=ContentType.PHOTO)

