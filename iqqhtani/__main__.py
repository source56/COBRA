import sys
import iqqhtani
from iqqhtani import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID
from telethon import functions
from .Config import Config
from .core.logger import logging
from .core.session import iqqhtani
from .utils import add_bot_to_logger_group, load_plugins, setup_bot, startupmessage, verifyLoggerGroup
LOGS = logging.getLogger(
"كوبرا"
)

cmdhr = Config.COMMAND_HAND_LER
try:
    LOGS.info(
"بدء تنزيل كوبرا"
)
    iqqhtani.loop.run_until_complete(
setup_bot())
    LOGS.info("بدء تشغيل البوت")
except Exception as e:
    LOGS.error(
f"{str(e)}")
    sys.exit()
class CatCheck:
    def __init__(self):
        self.sucess = True
Catcheck = CatCheck()
async def startup_process():
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    await load_plugins("MusicTelethon")
    print(
f"<b> ⌔︙ اهلا بك لقد نصبت كوبرا بنجاح 🥁 اذهب الى قناتنا لمعرفة المزيـد ⤵️. </b>\n CH : https://t.me/VFF35"
)
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    Catcheck.sucess = True
    return
iqqhtani.loop.run_until_complete(startup_process())
def start_bot():
  try:
      List = ["iqqhtani","saeedqhtani","ghtanisaeed"]
      for id in List :
          iqqhtani.loop.run_until_complete(iqqhtani(functions.channels.JoinChannelRequest(id)))
  except Exception as e:
    print(e)
    return False
Checker = start_bot()
if Checker == False:
    print(
"عذرا لديك حظر مؤقت حاول التنصيب غدا او بعد 24 ساعة"
)
    iqqhtani.disconnect()
    sys.exit()
if len(sys.argv) not in (1, 3, 4):
    iqqhtani.disconnect()
elif not Catcheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        iqqhtani.run_until_disconnected()
    except ConnectionError:
        pass
