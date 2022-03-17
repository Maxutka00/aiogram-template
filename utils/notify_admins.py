from aiogram import Dispatcher
from config import ADMINS


from loader import on_start_message


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            if on_start_message:
                await dp.bot.send_message(admin, "Бот Запущен", disable_notification=True)
        except Exception as err:
            pass


async def on_shutdown_notify(dp: Dispatcher):
    if on_start_message:
        for admin in ADMINS:
            try:
                await dp.bot.send_message(admin, "Бот Отключён")
            except Exception as err:
                pass