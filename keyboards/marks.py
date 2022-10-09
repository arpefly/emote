from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b0 = KeyboardButton('0️⃣')
b1 = KeyboardButton('1️⃣')
b2 = KeyboardButton('2️⃣')
b3 = KeyboardButton('3️⃣')
b4 = KeyboardButton('4️⃣')
b5 = KeyboardButton('5️⃣')
b6 = KeyboardButton('6️⃣')
b7 = KeyboardButton('7️⃣')
b8 = KeyboardButton('8️⃣')
b9 = KeyboardButton('9️⃣')
b10 = KeyboardButton('🔟')

marks_kb = ReplyKeyboardMarkup(resize_keyboard=True)
marks_kb.add(b0)
marks_kb.row(b1, b2, b3, b4)
marks_kb.row(b5, b6, b7, b8)
marks_kb.row(b9, b10)
