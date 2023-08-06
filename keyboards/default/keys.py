from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup

sl_cst = ReplyKeyboardMarkup(
    keyboard=[
      [
        KeyboardButton("Seller"),
        KeyboardButton("Customer"),
      ],
    ],

    resize_keyboard=True,
    one_time_keyboard=True
)


