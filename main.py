
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio, os

TOKEN = os.getenv("TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["📍 Найти терминал", "💰 Оценить золото", "🛒 Купить слиток", "📤 Продать золото", "👤 Мои заявки"]
    keyboard.add(*[types.KeyboardButton(text=b) for b in buttons])
    await message.answer("👋 Добро пожаловать в GOLDEXROBOT!
Выберите действие:", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
