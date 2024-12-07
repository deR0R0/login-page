import sys
import os
from flask import jsonify, request
from flask_cors import CORS
import logging

# Import utils
from utils.Config import *
from utils.Filer import File, Filer
from utils.UserManager import UManager
from utils.LogManager import Logger

cors = CORS(app, resources={r"/login-page/api/*": {"origins": "*"}})

# Get path based on stuff (differences between windows and mac/linux and stuf)
def getPath():
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
        return application_path
    return os.path.dirname(os.path.abspath(__file__))

# 404 Page
@app.errorhandler(404)
def notFound(e):
    return "404 - Page Not Found", 404


# Remove the logging
logging.getLogger("werkzeug").setLevel(logging.ERROR)


# High Seas - Login Page Stuff

# TODO:
# 1. Create homepage
# 2. Check token in login page
# 3. Rate limit

# Login
@app.route("/login-page/api/login", methods=["GET", "POST"])
def loginPageApiLogin():
    # Log the request
    Logger.log("MAINPROCESS", f"Recieved {request.method} from {request.remote_addr} for login")
    # Get Response after Attempting to login User!
    r = UManager.loginUser(request.args.get("username"), request.args.get("password"))
    match r:
        case "unknownUser":
            return jsonify({"status": 403, "error": "invalidUserPass", "token": None})
        case "invalidPassword":
            return jsonify({"status": 403, "error": "invalidUserPass", "token": None})
        case _:
            return jsonify({"status": 200, "error": None, "token": r}) # Finally!
        

# Signup
@app.route("/login-page/api/signup", methods=["GET", "POST"])
def loginPageApiSignup():
    # Log the request
    Logger.log("MAINPROCESS", f"Recieved {request.method} from {request.remote_addr} for signup")
    # Get Response after Attempting to login User!
    r = UManager.signupUser(request.args.get("username"), request.args.get("password"))
    match r:
        case "usernameExists":
            return jsonify({"status": 499})
        case _:
            return jsonify({"status": 200}) # Finally!
        
# Sign out
@app.route("/login-page/api/signout", methods=["GET", "POST"])
def loginPageApiSignout():
    # Log Request
    Logger.log("MAINPROCESS", f"Recieved {request.method} from {request.remote_addr} for signout")
    # Get Reponse of thing
    UManager.signOut(request.args.get("token"))
    return jsonify({"status": "200"})


# Get data
@app.route("/login-page/api/user", methods=["GET", "POST"])
def loginPageApiUser():
    # Log Request
    Logger.log("MAINPROCESS", f"Recieved {request.method} from {request.remote_addr} for user")
    # Get Reponse of thing
    r = UManager.getUserData(request.args.get("token"))
    match r:
        case "invalidToken":
            return jsonify({"status": 403})
        case _:
            return jsonify({"status": 200, "name": r[0], "pass": r[1], "token": request.args.get("token")})
       


# Set Path
Logger.setPath(getPath())
Filer.setPath(getPath())

if __name__ == "__main__":
    # Load users (for high seas login page)
    UManager.readUserData()
    # Run Server
    app.run(host="0.0.0.0", port=80)