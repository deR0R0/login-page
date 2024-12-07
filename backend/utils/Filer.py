import json

# import utils
from utils.Config import *

programPath = ""

class Filer:
    @staticmethod
    def setPath(path: str) -> None:
        global programPath
        programPath = path

class File:
    def __init__(self, file_name: str, file_type: str):
        self.file_name = file_name
        self.file_type = file_type
        
    def readFile(self) -> any:
        try: # Attempt to read
            with open(f"{programPath}/data/{self.file_name}.{self.file_type}", 'r') as f:
                if self.file_type == "json":
                    return json.load(f)
                elif self.file_type == "txt":
                    return f.read()
                else:
                    return "Unknown File Type"
        except FileNotFoundError: # File isn't found!
            match self.file_type:
                case "json":
                    contents = {}
                case _:
                    contents = ""

            # Creates file
            self.writeFile(contents)

            # Call read file again
            return self.readFile()

    
    def writeFile(self, content: any) -> None:
        with open(f"{programPath}/data/{self.file_name}.{self.file_type}", 'w') as f:
            if self.file_type == "json":
                json.dump(content, f, ensure_ascii = False, indent = 4)
                return
            elif self.file_type == "txt":
                f.write(content)
                return
            else:
                return "Unknown File Type"