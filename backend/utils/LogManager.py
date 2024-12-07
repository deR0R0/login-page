import datetime
from colorama import Fore as fore

from utils.Config import *

programPath = ""

# Class
class Logger:
    @staticmethod
    def setPath(path: str):
        global programPath
        programPath = path

    @staticmethod
    def addToLogs(prefix: str, msg: str) -> None:
        global programPath

        try:
            with open(f"{programPath}/data/{logFileName}", 'a') as f:
                f.write(f"{prefix} | {msg}\n")
        except FileNotFoundError:
            with open(f"{programPath}/data/{logFileName}", 'w') as f:
                f.write(f"{prefix} | {msg}\n")
        except Exception as err:
            # What...
            Logger.err("LogManager", f"Error while writing file: {err}")


    @staticmethod
    def log(location: str, msg: str) -> None:
        # Print and call to the add to logs :)
        # For normal stuff
        print(f"{dateColor}{dateFormat} {logColor} INFO | LOCATION: {location.upper()} | {fore.WHITE}{msg}")
        #Logger.addToLogs(prefix=f"{dateFormat} INFO | LOCATION: {location.upper()}", msg=msg)
    
    @staticmethod
    def warn(location: str, msg: str) -> None:
        # Print and call to the add to logs :)
        # For handled exceptions
        print(f"{dateColor}{dateFormat} {warnColor} INFO | LOCATION: {location.upper()} | {fore.WHITE}{msg}")
        #Logger.addToLogs(prefix=f"{dateFormat} INFO | LOCATION: {location.upper()}", msg=msg)

    @staticmethod
    def err(location: str, msg: str) -> None:
        # Print and call to the add to logs :)
        # For unhandled exceptions
        print(f"{dateColor}{dateFormat} {errColor} INFO | LOCATION: {location.upper()} | {fore.WHITE}{msg}")
        #Logger.addToLogs(prefix=f"{dateFormat} INFO | LOCATION: {location.upper()}", msg=msg)