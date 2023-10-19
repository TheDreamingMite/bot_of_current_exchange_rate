from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command

import db
import kb
import text
import utils


# class Form(StatesGroup):
#     peremennaya = State() # Задаем состояние


router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(db.start_bd(msg.from_user.full_name))  # регистрация нового пользователя
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)
    print(msg)

@router.message(Command("all_users"))
async def users(msg: Message):
    await msg.answer(db.all_usres())

@router.message((F.text == "Список пользователей")&(F.from_user.username == 'theDreamingMite'))
async def users2(msg: Message):
    await msg.answer(db.all_usres())
    print("eee")

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.callback_query(F.data == "current_exchange_rate")
async def input_text_prompt1(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.edit_text("Выполняется определение курса...")
    await clbck.message.answer(utils.calc_rate(), reply_markup=kb.enter_kb)

@router.callback_query(F.data == "account_with_commission")
async def input_text_prompt2(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.edit_text("Напишите количество долларов для расчета с комиссией")

@router.message(lambda message: message.text.isdigit())
async def process_amount3(message: Message):
    print('!')
    amount = float(message.text)
    total = utils.calc_with_comission(amount)
    if(utils.calc_with_comission(amount)[2] == 0):
        await message.answer("Сервисы недоступны")
    await message.answer(f"Сумма с комиссией: {utils.calc_with_comission(amount)[0]:.1f} руб. \nКомиссия: {utils.calc_with_comission(amount)[1]}%\nКурс доллара: {utils.calc_with_comission(amount)[2]:.1f} руб.")

@router.callback_query(F.data == "change_data")
async def input_text_prompt4(clbck: CallbackQuery, state: FSMContext):
    print('!!')
    await clbck.message.edit_text("Выполняется поиск пользователя...")
    #await clbck.answer(db.change_data(F.from_user.first_name,commission))
    await clbck.message.edit_text("Напишите комиссию")
    # await Form.peremennaya.set()  # Устанавливаем состояние

#считывание новой комиссии
# @router.message(lambda message: message.text.isdigit()) #,state=Form.a) # Принимаем состояние
# async def process_amount3(message: types.Message, state: FSMContext):
    # async with state.proxy() as proxy: # Устанавливаем состояние ожидания
    # a['peremennaya'] = message.text
    # await state.finish() # Выключаем состояние
    # print('!%%')

# @router.message_handler(commands=['start'])
# async def start(message: types.Message):
#     await bot.send_message(message.chat.id, 'Отправь свое сообщение:')
#     await Form.peremennaya.set() # Устанавливаем состояние
#
# @router.message_handler(state=Form.a) # Принимаем состояние
# async def start(message: types.Message, state: FSMContext):
#     async with state.proxy() as proxy: # Устанавливаем состояние ожидания
#     a['peremennaya'] = message.text
#     await state.finish() # Выключаем состояние
