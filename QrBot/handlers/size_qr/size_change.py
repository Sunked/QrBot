from aiogram import Router, F
from aiogram.types import Message
import keyboards as KB

router = Router()

_format = (360, 550) # for medium size
size = 5


@router.message(F.text.lower() == "small")
async def small(msg: Message):
    global size, _format
    _format = (400, 560)
    size = 1
    await msg.answer("You changed the size to small")


@router.message(F.text.lower() == "medium")
async def medium(msg: Message):
    global size, _format
    size = 5
    _format = (360, 550)
    await msg.answer("You changed the size to medium")


@router.message(F.text == "large")
async def large(msg: Message):
    global size, _format
    _format = (180, 345)
    size = 15
    await msg.answer("You changed the size to large")