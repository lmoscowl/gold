
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'ТВОЙ_ТОКЕН_ТУТ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["📈 Курс золота", "🪙 Купить слиток"]
    keyboard.add(*buttons)
    await message.answer("👋 Добро пожаловать в GOLDEXROBOT!", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "📈 Курс золота")
async def get_price(message: types.Message):
    await message.answer("📊 Текущий курс золота: 7400₽/грамм")

@dp.message_handler(lambda message: message.text == "🪙 Купить слиток")
async def buy_gold(message: types.Message):
    await message.answer("💰 Отлично! Свяжитесь с оператором для покупки.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
