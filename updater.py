import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import datetime
import requests

load_dotenv(dotenv_path='config/.env')

TOKEN = os.getenv('TOKEN')
WTOKEN = os.getenv('UPDATE_TOKEN')
prefix = '*'
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
#########################################################

def refresh():
    num2 = 0
    tmember = 0
    for i in bot.guilds:
        server = bot.guilds[num2]
        if server.id in [834445430669574234, 798857253934858269]:
            pass
        else:
            tmember = tmember + int(server.member_count)

        num2 = num2 + 1

    return {"servers":len(bot.guilds),"users":tmember}

@bot.event
async def on_ready():
    print('I am ready')


@bot.command()
async def update(ctx):
    datet = datetime.datetime.today()

    data = refresh()
    requests.get("https://memeshubapi.herokuapp.com/update?token="+WTOKEN, params=data)
    print("DATA POSTED")

bot.run(TOKEN)