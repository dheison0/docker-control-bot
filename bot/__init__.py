from dotenv import load_dotenv
from os import getenv
from logging import warn

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN", "")
assert BOT_TOKEN != ""
ADMINISTRATORS = getenv("ADMINS", "").split()
if len(ADMINISTRATORS) == 0:
    warn("O sistema está aberto para todo mundo!")