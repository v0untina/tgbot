import asyncio

from aiogram import Bot,Dispatcher,F
from aiogram.filters import Command
from aiogram.types import Message

bot=Bot("6901646684:AAHGW8TwMwJaAdnK38blPejh1Ch_ZNNJSlU",parse_mode="HTML")
dp=Dispatcher()

@dp.message(Command("start"))
async def start(message:Message):
    await message.answer("ТЕСТ")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__=="__main__":
    asyncio.run(main())