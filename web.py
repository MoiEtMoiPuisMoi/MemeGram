import os
from dotenv import load_dotenv
from flask import Flask, request, render_template

load_dotenv(dotenv_path='config/.env')

app = Flask(__name__)
TOKEN = os.getenv('TOKEN')
WTOKEN = os.getenv('UPDATE_TOKEN')

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

jfile = {"servers":"None", "users":"None"}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', users=jfile["users"], servers=jfile["servers"])

@app.route('/api')
def api():
    return jfile

@app.route('/update')
def update():
    token = request.args.get('token')
    servers = request.args.get('servers')
    users = request.args.get('users')
    if token == WTOKEN:
        jfile["servers"] = servers
        jfile["users"] = users
        return jfile
    else:
        return {"error":"ACCES DENIED"}

if __name__ == "__main__":
    app.run()