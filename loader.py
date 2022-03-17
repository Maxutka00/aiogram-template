import json
import os
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config
from utils.db_api.db import ActionWithDB


def load_data(data_file):
    with open(os.path.join("data", f"{data_file}.json"), "r") as f:
        config = json.load(f)
    return config["token"], config["on_start_message"]

def set_token():
    global mode
    args = sys.argv
    if len(args) > 1:
        try:
            return load_data(args[1])
        except Exception:
            raise Exception('No such configuration file')
    else:
        return load_data("default")



BOT_TOKEN, on_start_message = set_token()



bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
db = ActionWithDB()
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)




