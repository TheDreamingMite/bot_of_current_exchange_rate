from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command

import db
import kb
import text
import utils

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)
    print(msg)
    db.start_bd(msg.from_user.full_name) #регистрация нового пользователя

@router.message(Command("users"))
async def start_handler(msg: Message):
    await msg.answer(db.all_usres(), reply_markup=kb.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.callback_query(F.data == "current_exchange_rate")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.edit_text("Выполняется определение курса...")
    await clbck.message.answer(utils.calc_rate(), reply_markup=kb.enter_kb)

@router.callback_query(F.data == "account_with_commission")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.edit_text("Напишите количество долларов для расчета с комиссией")

@router.message(lambda message: message.text.isdigit())
async def process_amount(message: Message):
            amount = float(message.text)
            total = utils.calc_with_comission(amount)
            if(utils.calc_with_comission(amount)[2] == 0):
                await message.answer("Сервисы недоступны")
            await message.answer(f"Сумма с комиссией: {utils.calc_with_comission(amount)[0]:.1f} руб. \nКомиссия:{utils.calc_with_comission(amount)[1]}\n%Курс доллара: :{utils.calc_with_comission(amount)[2]:.1f} руб.")

@router.callback_query(F.data == "change_data")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.edit_text("Выполняется поиск пользователя...")
