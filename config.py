import os

API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

OWNER = int(os.environ.get("OWNER", "0"))
LOG = int(os.environ.get("LOG", "0"))

PASS_DB = int(os.environ.get("PASS_DB", "721"))

ADMINS = []

try:
    admins_raw = os.environ.get("ADMINS", "")
    for admin in admins_raw.replace(",", " ").split():
        if admin.strip():
            ADMINS.append(int(admin.strip()))
except ValueError:
    raise Exception("ADMINS must contain only numbers.")

if OWNER != 0 and OWNER not in ADMINS:
    ADMINS.append(OWNER)
