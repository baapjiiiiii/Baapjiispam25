from os import getenv
from dotenv import load_dotenv

load_dotenv()

STRING = getenv("STRING")
STRING2 = getenv("STRING2")
STRING3 = getenv("STRING3")
STRING4 = getenv("STRING4")
STRING5 = getenv("STRING5")
STRING6 = getenv("STRING6")
STRING7 = getenv("STRING7")
STRING8 = getenv("STRING8")
STRING9 = getenv("STRING9")
STRING_10 = getenv("STRING10")
ALIVE_NAME = getenv("ALIVE_NAME")
API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
CMD_HNDLR = getenv("CMD_HNDLR")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
ALIVE_PIC = getenv("ALIVE_PIC")
BIO_MESSAGE = getenv("BIO")
SUDO_USERS= list(map(int, getenv("SUDO_USERS").split()))
