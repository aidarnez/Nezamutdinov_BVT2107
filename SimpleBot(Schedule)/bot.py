from aiogram import Bot, Dispatcher, executor, types
from timetable import tomorrow_timetable, week_timetable
import datetime
# Объект бота
bot = Bot(token="1994932843:AAG1Rwjn4S6PLOzAB2MrjMfOAErNc8XGOoU")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
# Хэндлер на команду
@dp.message_handler(commands="tomorrow")
async def tomorrow(message: types.Message):
    tomorrow_date = datetime.date.today() + datetime.timedelta(days=1)  # Tomorrow date
    tomorrow_day = datetime.date.weekday(tomorrow_date)
    t = tomorrow_timetable(tomorrow_day)
    await message.reply(t)

@dp.message_handler(commands="today")
async def today(message: types.Message):
    today_date = datetime.date.today()  # Tomorrow date
    today_day = datetime.date.weekday(today_date)
    t = tomorrow_timetable(today_day)
    await message.reply(t)

@dp.message_handler(commands="week")
async def week(message: types.Message):
    for day in range(6):
        t = week_timetable(day)
        await message.reply(t)

@dp.message_handler(commands="help")
async def week(message: types.Message):
    await message.reply("Я могу оптравить тебе расписание занятий у группы БВТ2107")

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)