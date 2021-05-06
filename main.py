import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from flask import Flask

load_dotenv(dotenv_path='config/.env')

app = Flask(__name__)
TOKEN = os.getenv('TOKEN')
prefix = 'fm!'
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

#########################################################
#         Bot devlopped by Moi#5013 on discord          #
#########################################################
#   __  __         _    _  _    ____    ___   _  _____  #
#  |  \/  |  ___  (_) _| || |_ | ___|  / _ \ / ||___ /  #
#  | |\/| | / _ \ | ||_  ..  _||___ \ | | | || |  |_ \  #
#  | |  | || (_) || ||_      _| ___) || |_| || | ___) | #
#  |_|  |_| \___/ |_|  |_||_|  |____/  \___/ |_||____/  #
#                                                       #
########################################################

@app.route('/')
def index():
    jfile = {"servers":"EXAMPLE", "users":"EXAMPLE"}
    jfile["servers"] = len(bot.guilds)
    return jfile

app.run(port=5000)