import colorama
from flask import Flask, render_template
import random
from meme import Meme
from datetime import datetime
from colorama import init
init()


app = Flask(__name__)

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

def SUCCESS():
    now = datetime.now()
    print(colorama.Fore.GREEN+"["+str(datetime.strptime("%d/%m/%Y %H:%M:%S"))+"Load Page succes - 200"+colorama.Fore.RESET)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/read', methods=['GET'])
def read():
    meme = Meme()
    return render_template('read.html', reddit_name=meme.subreddit, image=meme.url, upvote=meme.ups, comments=random.randint(100, 1000), minute=random.randint(1, 59))

if __name__ == "__main__":
    app.run()
