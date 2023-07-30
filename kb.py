from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove
from aiogram import types
# - - - Меню - - -
menu = [
    [InlineKeyboardButton(text="Ипотека 🏡", callback_data="ipo")],
    [InlineKeyboardButton(text="Топ акций застройщиков 📋", callback_data="akz")],
    [InlineKeyboardButton(text="Подборки комплексов 🏙", callback_data="podbor")],
    [InlineKeyboardButton(text="FAQ", callback_data="faq")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
# - - - Связь - - -
call_din = [
    [types.KeyboardButton(text='Связь 📞')],
]
call_din = types.ReplyKeyboardMarkup(keyboard=call_din, resize_keyboard=True, input_field_placeholder='Навигация')

call = [
    [InlineKeyboardButton(text='Связаться с менеджером 👩🏻', url='t.me/@alena_d_s')],
    [InlineKeyboardButton(text='Связаться с ипотечным специалистом 👩🏻', url='t.me/@arthouse_admin')],
    [InlineKeyboardButton(text='Наш сайт 🌐', url='https://a-house.storee')],
    [InlineKeyboardButton(text='Наш Telegram-канал 🔗', url='https://t.me/@arthousespb')],
    [InlineKeyboardButton(text='В главное меню ↩️', callback_data="menu")]
]
call = InlineKeyboardMarkup(inline_keyboard=call)
# - - - Ипотека - - -
ipo = [
    [InlineKeyboardButton(text='Кредитная история 📋', callback_data="ipo_kred")],
    [InlineKeyboardButton(text='Программы ипотеки 🗂', callback_data="ipo_prog")],
    [InlineKeyboardButton(text='Бесплатное одобрение 🔖', callback_data="ipo_free")],
    [InlineKeyboardButton(text='Ипотечный калькулятор 🖥', callback_data="ipo_calc")],
    [InlineKeyboardButton(text='в Главное меню ↩️', callback_data="menu")]
]
ipo = InlineKeyboardMarkup(inline_keyboard=ipo)
# - - - Меню -> Ипотека -> Кредитная история - - -
ipo_kred = [
    [InlineKeyboardButton(text='Проверка кредитной истории 📋', callback_data="ipo_kred1")],
    [InlineKeyboardButton(text='Для чего её знать и как улучшить ❓', callback_data="ipo_kred2")],
    [InlineKeyboardButton(text='Вернуться назад 🔙', callback_data="back_ipo")],
    [InlineKeyboardButton(text='Вернуться в главное меню ↩️', callback_data="menu")]
]
ipo_kred = InlineKeyboardMarkup(inline_keyboard=ipo_kred)
# - - - Меню -> Ипотека -> Кредитная история -> Проверка кредитной истории
ipo_kred1 = [
    [InlineKeyboardButton(text='Вернуться назад 🔙', callback_data="back_kred")],
    [InlineKeyboardButton(text='Вернуться в главное меню ↩️', callback_data="menu")]
]
ipo_kred1 = InlineKeyboardMarkup(inline_keyboard=ipo_kred1)
# - - - Меню -> Ипотека -> Кредитная история -> Для чего её знать и как улучшить
ipo_kred2 = [
    [InlineKeyboardButton(text='Вернуться назад 🔙', callback_data="back_kred")],
    [InlineKeyboardButton(text='Вернуться в главное меню ↩️', callback_data="menu")]
]
ipo_kred2 = InlineKeyboardMarkup(inline_keyboard=ipo_kred2)
# - - - Меню -> Ипотека -> Программы по ипотеке - - -
ipo_prog = [
    [InlineKeyboardButton(text='Описание программ 🗞', callback_data="ipo_prog1")],
    [InlineKeyboardButton(text='Узнать свою программу 📈', callback_data="ipo_prog2")],
    [InlineKeyboardButton(text='Вернуться назад 🔙', callback_data="back_ipo")],
    [InlineKeyboardButton(text='Вернуться в главное меню ↩️', callback_data="menu")]
]
ipo_prog = InlineKeyboardMarkup(inline_keyboard=ipo_prog)
# - - - Меню -> Ипотека -> Программы по ипотеке -> Описание программ
ipo_prog1 = [
    [InlineKeyboardButton(text='Вернуться назад 🔙', callback_data="back_kred")],
    [InlineKeyboardButton(text='Вернуться в главное меню ↩️', callback_data="menu")]
]
ipo_prog1 = InlineKeyboardMarkup(inline_keyboard=ipo_prog1)
# - - - Меню -> Ипотека -> Программы по ипотеке -> Узнать свою программу
ipo_prog2 = [
    [InlineKeyboardButton(text='Вернуться назад 🔙', callback_data="back_kred")],
    [InlineKeyboardButton(text='Вернуться в главное меню ↩️', callback_data="menu")]
]
ipo_prog2 = InlineKeyboardMarkup(inline_keyboard=ipo_prog2)
# - - - Меню -> Ипотека -> Бесплатное одобрение
ipo_free = [
    [InlineKeyboardButton(text='Вернуться назад 🔙', callback_data="back_ipo")],
    [InlineKeyboardButton(text='Вернуться в главное меню ↩️', callback_data="menu")]
]
ipo_free = InlineKeyboardMarkup(inline_keyboard=ipo_free)
# - - - Меню -> Ипотека -> Ипотечный калькулятор
ipo_calc = [
    [InlineKeyboardButton(text='Вернуться назад 🔙', callback_data="back_ipo")],
    [InlineKeyboardButton(text='Вернуться в главное меню ↩️', callback_data="menu")]
]
ipo_calc = InlineKeyboardMarkup(inline_keyboard=ipo_calc)
# - - - Меню -> Топ акций застройщиков
akz = [
    [InlineKeyboardButton(text='Вернуться в главное меню ↩️', callback_data="menu")]
]
akz = InlineKeyboardMarkup(inline_keyboard=akz)
# - - - Меню -> Подборки комплексов
podbor = [
    [InlineKeyboardButton(text='Вернуться в главное меню ↩️', callback_data="menu")]
]
podbor = InlineKeyboardMarkup(inline_keyboard=podbor)
# - - - Меню -> Антикейсы
faq = [
    [InlineKeyboardButton(text='Вернуться в главное меню ↩️', callback_data="menu")]
]
faq = InlineKeyboardMarkup(inline_keyboard=faq)
# - - - Кнопки Связь и Главное меню
back_1 = [
    [types.KeyboardButton(text='Главное меню ↩️'),
     types.KeyboardButton(text='Связь 📞')],
]
back_1 = types.ReplyKeyboardMarkup(keyboard=back_1, resize_keyboard=True)