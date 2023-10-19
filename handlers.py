from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command

import kb
import text
import utils

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

    async def cmd_start(message: Message):
        kb = [
            [KeyboardButton(text="Курс")],
            [KeyboardButton(text="Расчет")]
        ]
        keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        await message.answer(                             reply_markup=keyboard)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.callback_query(F.data == "current_exchange_rate")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.edit_text(utils.calc_rate())




