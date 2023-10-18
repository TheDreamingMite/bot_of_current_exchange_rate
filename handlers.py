from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

import kb
import text

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.callback_query(F.data == "current_exchange_rate")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.text_prompt)
    await clbck.message.edit_text(text.gen_text)
    await clbck.message.answer(text.gen_exit, reply_markup=kb.exit_kb)

# Обработчки кнопки "Нынешний курс"
@router.callback_query(F.data == "current_exchange_rate")
async def get_exchange_rate(message: Message):
    for n in range(1, 3):
        exchange_rate = cache.get(n)
        if exchange_rate is not None:
            # Обращение в кэш
            await message.answer(f"На {date.today()} курс доллара составляет: {exchange_rate:.1f} руб.")
            break

        exchange_rate = get_from_api(API_URL[n], n)
        if exchange_rate is not None:
            await message.answer(f"На {date.today()} курс доллара составляет: {exchange_rate:.1f} руб.")
            break
        elif n == 2:
            await message.answer("Ошибка, ни один источник данных не доступен")


