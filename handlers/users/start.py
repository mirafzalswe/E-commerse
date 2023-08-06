from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart


from keyboards.default.keys import sl_cst
from loader import dp
from states.regist import St_Customser, SellerState

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await message.answer("Kim bolip kirmoxchisiz ?", reply_markup=sl_cst)


@dp.message_handler(text='Customer')
async def regist_c(message: types.Message):
    await message.answer("isimgizni kiritng: ")
    await St_Customser.name.set()

@dp.message_handler(state=St_Customser.name)
async def load_name(message: types.Message, state:FSMContext) -> None:
    async with state.proxy() as data:
        data['name'] = message.text

    await message.reply("Yashash manilingizni kiring: ")
    await St_Customser.next()


@dp.message_handler(state=St_Customser.address)
async def load_address(message:types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['address'] = message.text

    await message.reply("Telefon raqamingizni kiriting: ")
    await St_Customser.next()

    @dp.message_handler(state=St_Customser.phone)
    async def load_contact(message: types.Message, state: FSMContext) -> None:
        async with state.proxy() as data:
            data['phone'] = message.text

        await message.reply("Ro'yaxtad ottingiz !")
        await state.finish()










@dp.message_handler(text='Seller')
async def regist_c(message: types.Message):
    await message.answer("isimgizni kiritng: ")
    await SellerState.name.set()

@dp.message_handler(state=SellerState.name)
async def load_name(message: types.Message, state:FSMContext) -> None:
    async with state.proxy() as data:
        data['name'] = message.text

    await message.reply("Yashash manilingizni kiring: ")
    await SellerState.next()

@dp.message_handler(lambda message:not message.text.isdigit(),state=SellerState)
async def check_age(message:types.Message):
    await message.reply("Bu raqam emas")

@dp.message_handler(lambda message:not message.text.isdigit(),state=St_Customser)
async def check_age(message:types.Message):
    await message.reply("Bu raqam emas")


@dp.message_handler(state=SellerState.address)
async def load_address(message:types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['address'] = message.text

    await message.reply("Telefon raqamingizni kiriting: ")
    await SellerState.next()

@dp.message_handler(state=SellerState.phone)
async def load_contact(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['phone'] = message.text

    await message.reply("Ro'yaxtad ottingiz !")
    await state.finish()





