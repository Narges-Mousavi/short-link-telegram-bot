from aiogram import Bot, Dispatcher, executor, types
import pyshorteners

bot = Bot('your bots API TOKEN')
dp = Dispatcher(bot)
sl =pyshorteners.Shortener()

@dp.message_handler(commands=['start', 'help'])
async def passwordmaker(pm: types.Message):
    await pm.answer("یه لینک برام بفرست تا برات کوتاهش کنم 😁")


@dp.message_handler()
async def shorter_link(pm: types.Message):
    await pm.answer("لطفا چند لحظه صبر کن موز موزی🍌😎😶‍🌫️")
    link = str(pm.text)
    shortlink = sl.osdb.short(link)
    print(shortlink)
    await pm.reply(shortlink)
if __name__ == '__main__':
    executor.start_polling(dp)
