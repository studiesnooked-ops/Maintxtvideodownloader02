import os

# Required Telegram values
API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Owner/Admin
OWNER = int(os.environ.get("OWNER", "0"))

ADMINS = []
try:
    for x in os.environ.get("ADMINS", "").replace(",", " ").split():
        if x.strip():
            ADMINS.append(int(x.strip()))
except ValueError:
    raise Exception("ADMINS must contain only Telegram user IDs.")

if OWNER and OWNER not in ADMINS:
    ADMINS.append(OWNER)

# Log channel/group ID
LOG = int(os.environ.get("LOG", "0"))

# Optional password/database value
PASS_DB = int(os.environ.get("PASS_DB", "721"))

# Optional update group
UPDATE_GRP = int(os.environ.get("UPDATE_GRP", "0"))


# Validation
if API_ID == 0:
    raise Exception("API_ID is missing in environment variables.")

if not API_HASH:
    raise Exception("API_HASH is missing in environment variables.")

if not BOT_TOKEN:
    raise Exception("BOT_TOKEN is missing in environment variables.")

if OWNER == 0:
    raise Exception("OWNER is missing in environment variables.")
