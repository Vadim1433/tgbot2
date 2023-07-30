from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

import kb
import text

router = Router()


@router.message(Command('start'))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.call_din)
    await msg.answer(text.greet1, reply_markup=kb.menu)


@router.message(F.text == "Связь 📞")
async def call(msg: Message):
    await msg.answer(text.call, reply_markup=kb.call)


@router.callback_query(F.data == "menu")
async def menu(callback: CallbackQuery):
    await callback.message.answer(text.greet1, reply_markup=kb.menu)
    await callback.answer("Вы в Главном меню")
    await callback.answer()


@router.callback_query(F.data == "ipo")
async def ipo(callback: CallbackQuery):
    await callback.message.answer(text.ipo, reply_markup=kb.ipo)
    await callback.answer("Вы в пункте Ипотека")
    await callback.answer()


@router.callback_query(F.data == "back_ipo")
async def ipo_back(callback: CallbackQuery):
    await callback.message.answer(text.ipo, reply_markup=kb.ipo)
    await callback.answer()


# - - - Меню -> Ипотека -> Кредитная история - - -
@router.callback_query(F.data == "ipo_kred")
async def ipo_kred(callback: CallbackQuery):
    await callback.message.answer(text.ipo_kred, reply_markup=kb.ipo_kred)
    await callback.answer()


@router.callback_query(F.data == "back_kred")
async def ipo_kredback(callback: CallbackQuery):
    await callback.message.answer(text.ipo_kred, reply_markup=kb.ipo_kred)
    await callback.answer()


@router.callback_query(F.data == "ipo_kred1")
async def ipo_kred1(callback: CallbackQuery):
    await callback.message.answer(text.ipo_kred1, reply_markup=kb.ipo_kred1)
    await callback.answer()


@router.callback_query(F.data == "ipo_kred2")
async def ipo_kred2(callback: CallbackQuery):
    await callback.message.answer(text.ipo_kred2, reply_markup=kb.ipo_kred2)
    await callback.answer()


# - - - Меню -> Ипотека -> Кредитная история - - -
@router.callback_query(F.data == "ipo_prog")
async def ipo_prog(callback: CallbackQuery):
    await callback.message.answer(text.ipo_prog, reply_markup=kb.ipo_prog)
    await callback.answer()


@router.callback_query(F.data == "ipo_prog1")
async def ipo_prog1(callback: CallbackQuery):
    await callback.message.answer(text.ipo_prog1, reply_markup=kb.ipo_prog1)
    await callback.answer()


@router.callback_query(F.data == "ipo_prog2")
async def ipo_prog2(callback: CallbackQuery):
    await callback.message.answer(text.ipo_prog2, reply_markup=kb.ipo_prog2)
    await callback.answer()

# - - - Меню -> Ипотека -> Бесплатное одобрение
@router.callback_query(F.data == "ipo_free")
async def ipo_free(callback: CallbackQuery):
    await callback.message.answer(text.ipo_free, reply_markup=kb.ipo_free)
    await callback.answer()


# - - - Меню -> Ипотека -> Ипотечный калькулятор
@router.callback_query(F.data == "ipo_calc")
async def ipo_calc(callback: CallbackQuery):
    await callback.message.answer(text.ipo_calc, reply_markup=kb.ipo_calc)
    await callback.answer()


# - - - Меню -> Топ акций застройщиков
@router.callback_query(F.data == "akz")
async def akz(callback: CallbackQuery):
    await callback.message.answer(text.akz, reply_markup=kb.akz)
    await callback.answer()


# - - - Меню -> Подборки комплексов
@router.callback_query(F.data == "podbor")
async def podbor(callback: CallbackQuery):
    await callback.message.answer(text.podbor, reply_markup=kb.podbor)
    await callback.answer()


# - - - Меню -> Антикейсы
@router.callback_query(F.data == "faq")
async def faq(callback: CallbackQuery):
    await callback.message.answer(text.faq, reply_markup=kb.faq)
    await callback.answer()


@router.message(F.text == "Вернуться в Главное меню ↩️")
async def menu(msg: Message):
    await msg.answer(text.greet1, reply_markup=kb.menu)


@router.message()
async def answer(msg: Message):
    await msg.answer("Я вас не понимаю. Если возникли трудности, перезапустите меня командой /start")
