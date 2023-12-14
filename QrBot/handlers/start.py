from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
import keyboards as KB

router = Router()

@router.message(Command("start"))
async def start(msg: Message):
    await msg.answer(f"""Hello, <b>{msg.from_user.full_name}</b>.
I'm a bot that can turn any source into qr-code.
Your can choose the size of your qr-code or make it in png format.""", reply_markup=KB.start)