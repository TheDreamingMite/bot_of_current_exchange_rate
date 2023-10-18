from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="📝 Курс доллара на сегодня", callback_data="current_exchange_rate"),
    InlineKeyboardButton(text="💰 Посчитать курс с учетом комиссии", callback_data="account_with_commission")],
    [InlineKeyboardButton(text="🔎 Изменить данные", callback_data="change_data")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])