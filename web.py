from flask import Flask, request, render_template
import random
from meme import Meme


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


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/read')
def index():
    meme = Meme()
    meme2 = Meme()
    meme3 = Meme()

    return render_template('read.html', reddit_name=meme.subreddit, image=meme.url, upvote=meme.ups, comments=random.randint(100, 1000), minute=random.randint(1, 59),
                           reddit_name2=meme2.subreddit, image2=meme2.url, upvote2=meme2.ups, comments2=random.randint(100, 1000), minute2=random.randint(1, 59),
                           reddit_name3=meme3.subreddit, image3=meme3.url, upvote3=meme3.ups, comments3=random.randint(100, 1000), minute3=random.randint(1, 59))

if __name__ == "__main__":
    app.run()