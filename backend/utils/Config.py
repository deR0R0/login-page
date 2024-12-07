import datetime
import time
from flask import Flask
from colorama import Fore as fore

# Logger Stuff
logFileName = "logs.txt"
logColor = fore.LIGHTBLUE_EX
warnColor = fore.LIGHTYELLOW_EX
errColor = fore.LIGHTRED_EX
dateColor = fore.LIGHTBLACK_EX
dateFormat = f"{datetime.datetime.now().replace(microsecond=0)}"

# Flask stuff
app = Flask(__name__)

# User Data - Yes, I use a single json file/dictionary...
# This is a super simple project and I don't feel like using SQL.
# Just Chill...
users = { "admin": "admin" }
usersTokens = { "admin": None }

usersSaveFile = "users"
usersTokensSaveFile = "userTokens"

# Token Stuff
tokenCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
tokenLength = 50


#while True:
#    print(programPath)
#    time.sleep(1)