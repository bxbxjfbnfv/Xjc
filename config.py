## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BACfbcKDdy0XQxRE004fUkUYWblbEAHTUlianT1HD0KWSskNGpO0d56UkXCZC9G4lXnb_3-q3K_QBOhKMYkkGuKia-5o-zd0HlrhfdTHMn1wVgb9fFAJbm3b6o5m4MmFF1NoWM4n_GxVXC9lh1ba8Zj5DMQlYnJgXLSk9BHjhoCNADOvhQC99ts3ZrYnuwCgU76lsrS7dgUhGsI0RQ-o9QixwVtHKaaIc8prl9NO-b9AdvAT7Zt7VdNzONx0Pt5c2ZbtcHKfmktPbIkG0dyEh-J2oHTz8wJrekz8KZjFJvlme55JPDeUrCtbzSV7JWwOTNS60L8Q2vECgD4qAH7xspHcAAAAAUS05_kA")
BOT_TOKEN = getenv("BOT_TOKEN", "5188955214:AAHIKiOLxPI1ZRLYxVMHe7h_U4VCtaB3b-A")
BOT_NAME = getenv("BOT_NAME", "Y_3_2_BOT")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "⦁𝗔ٰٖ𝗟ٰٖ𝗦ٰٖ𝗛ٰٖ𝗔ٰٖ𝗬ٰٖ𝗘ٰٖ𝗕ٰٖ ➪🇳🇱⦁")
OWNER_USERNAME = getenv("OWNER_USERNAME", "lIllIIllll")
ALIVE_NAME = getenv("ALIVE_NAME", "⦁𝗔ٰٖ𝗟ٰٖ𝗦ٰٖ𝗛ٰٖ𝗔ٰٖ𝗬ٰٖ𝗘ٰٖ𝗕ٰٖ ➪🇳🇱⦁")
BOT_USERNAME = getenv("BOT_USERNAME", "Playvideo1BoT")
OWNER_ID = getenv("OWNER_ID", "5373530553")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "M_4_44")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "x_0_00")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "x_0_00")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/466de30ee0f9383c8e09e.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/d70bb6fa92728763c671f.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
