import random

from utils.LogManager import Logger
from utils.Filer import File
import utils.Config as Config

uf = File(Config.usersSaveFile, "json")
utf = File(Config.usersTokensSaveFile, "json")

class UManager:

    # Save Users to File
    @staticmethod
    def saveUsersToFile() -> None:
        global uf
        global utf

        uf.writeFile(Config.users)
        utf.writeFile(Config.usersTokens)

    # Read and Set Stuff
    @staticmethod
    def readUserData() -> None:
        global uf
        global utf

        Config.users = uf.readFile()
        Config.usersTokens = utf.readFile()

    # Method name pretty self-explanatory
    @staticmethod
    def checkUserExists(name: str) -> bool:
        for user in Config.users.keys():
            if user == name:
                return True
        
        return False
    

    # Login User using Username and Password...
    @staticmethod
    def loginUser(u: str, p: str) -> str:
        try:
            # Check Exist
            if not UManager.checkUserExists(u):
                Logger.log("UserManager", f"Username {str(u)} doesn't exist!")
                return "unknownUser"
            
            # Check password
            if Config.users[u] != p:
                Logger.log("UserManager", f"User {str(u)} unsuccessfully attempted to log in with the password {str(p)}.")
                return "invalidPassword"
            
            # Correct pass and user!
            # Create token, set it, then return the token
            # Yes, it's random.choice, I do not want to make my own pseudorandom algo
            # FUTURE PLANS: Create Token Maker that has unix time in front and convert to base64
            token = ""
            for i in range(Config.tokenLength):
                token = token + random.choice(Config.tokenCharacters)
            
            Config.usersTokens[u] = token
            UManager.saveUsersToFile()
            return token
        except Exception as err:
            Logger.err(err)
            return "err"
    
    # Sign Up
    @staticmethod
    def signupUser(u: str, p: str) -> str:
        # Check Exist
        if UManager.checkUserExists(u):
            Logger.log("UserManager", "Username already exists!")
            return "usernameExists"
        
        # Create User
        Logger.log("UserManager", f"Created a user with the name: {u}")
        Config.users[u] = p

        # Save
        UManager.saveUsersToFile()

        return "success"
    
        # wow! super simple!

    # Signout
    @staticmethod
    def signOut(token: str) -> any:
        # Check token
        for user in Config.usersTokens.keys():
            if Config.usersTokens[user] == token:
                Config.usersTokens[user] = None
                Logger.log("UserManager", f"{user} is signing out!")
                return "success"
            
        return "tokenInvalid"

    # Get User Data
    @staticmethod
    def getUserData(token: str) -> any:
        Logger.log("UserManager", f"Checkin out token: {token}")
        # Check Token
        for user in Config.usersTokens.keys():
            if Config.usersTokens[user] == str(token):
                return [user, Config.users[user]]
        
        return "invalidToken"