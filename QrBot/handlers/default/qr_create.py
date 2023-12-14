import os

import aiogram.exceptions
from qrcode.main import QRCode # pip install qrcode
from PIL import Image # pip install Pillow
from aiogram import Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.types.input_file import FSInputFile

import keyboards as KB
from handlers.size_qr import size_change

router = Router()

@router.message()
async def create(msg: Message, bot: Bot):
    qr = QRCode(version=size_change.size)
    qr.make()
    qr.add_data(msg.text)
    qrcode = qr.make_image()

    path_qr = os.path.join("QrBot", "init_qrcodes", str(msg.from_user.id) + ".png")
    path_usr = os.path.join("QrBot", "init_images", "user_images", str(msg.from_user.id) + ".jpg")
    qrcode.save(path_qr)

    with Image.open(path_qr) as img_qr:
        if "telegram." in msg.text.lower() or "t.me" in msg.text.lower() or "tlgrm." in msg.text.lower():
            with Image.open(os.path.join("QrBot", "init_images", "telegram.jpg")) as img_tg:
                img_tg.paste(im=img_qr, box=size_change._format)
                img_tg.save(path_usr)
        
            await msg.answer_photo(photo=FSInputFile(path_usr), reply_markup=KB.png)
            os.remove(path_usr)

        elif "instagram." in msg.text.lower():
            with Image.open(os.path.join("QrBot", "init_images", "instagram.jpg")) as img_tg:
                img_tg.paste(im=img_qr, box=size_change._format)
                img_tg.save(path_usr)
        
            await msg.answer_photo(photo=FSInputFile(path_usr), reply_markup=KB.png)
            os.remove(path_usr)

        elif "twitch." in msg.text.lower():
            with Image.open(os.path.join("QrBot", "init_images", "twitch.jpg")) as img_tg:
                img_tg.paste(im=img_qr, box=size_change._format)
                img_tg.save(path_usr)
        
            await msg.answer_photo(photo=FSInputFile(path_usr), reply_markup=KB.png)
            os.remove(path_usr)

        elif "youtube." in msg.text.lower():
            with Image.open(os.path.join("QrBot", "init_images", "youtube.jpg")) as img_tg:
                img_tg.paste(im=img_qr, box=size_change._format)
                img_tg.save(path_usr)
        
            await msg.answer_photo(photo=FSInputFile(path_usr), reply_markup=KB.png)
            os.remove(path_usr)

        elif "google." in msg.text.lower():
            with Image.open(os.path.join("QrBot", "init_images", "google.jpg")) as img_tg:
                img_tg.paste(im=img_qr, box=size_change._format)
                img_tg.save(path_usr)
        
            await msg.answer_photo(photo=FSInputFile(path_usr), reply_markup=KB.png)
            os.remove(path_usr)

        elif "mail." in msg.text.lower():
            with Image.open(os.path.join("QrBot", "init_images", "mail.jpg")) as img_tg:
                img_tg.paste(im=img_qr, box=size_change._format)
                img_tg.save(path_usr)
        
            await msg.answer_photo(photo=FSInputFile(path_usr), reply_markup=KB.png)
            os.remove(path_usr)

        else:
            with Image.open(os.path.join("QrBot", "init_images", "rest.jpg")) as img_tg:
                img_tg.paste(im=img_qr, box=size_change._format)
                img_tg.save(path_usr)
        
            await msg.answer_photo(photo=FSInputFile(path_usr), reply_markup=KB.png)
            os.remove(path_usr)

    
@router.callback_query()
async def png_handler(query: CallbackQuery):
    path = os.path.join("QrBot", "init_qrcodes", str(query.from_user.id) + ".png")
    try:
        await query.message.answer_photo(photo=FSInputFile(path), caption="<b>Your png result</b>")
        os.remove(path)

    except aiogram.exceptions.TelegramNetworkError:
        await query.message.reply("sorry, but I don't have your qr code")