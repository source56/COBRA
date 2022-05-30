import re
import time
from datetime import datetime
from iqqhtani import StartTime, iqqhtani
from iqqhtani.Config import Config
from iqqhtani.plugins import mention
help1 = ("**♛ ⦙ كيفيه التنصيب :**")
help2 = ("**♛ ⦙ قـائمـه الاوامـر :**\n**♛ ⦙ قنـاه السـورس :** @VFF35\n**♛ ⦙ شـرح اوامـر السـورس : @VFF34**\n**♛ ⦙ شـرح فـارات السـورس : @VFF34** \n - اوامر الاونلاين تشتغل فقط في المجموعات ")
TG_BOT = Config.TG_BOT_USERNAME
TM = time.strftime("%I:%M")
Sour = f"**♛ : version 7.6  𓇡.** \n♛ : me  {mention}  𓇡. \n**♛ : time  {TM}  𓇡.**\n**♛ : My Bot {TG_BOT} 𓇡.**\n**♛ : Source : @VFF34  𓇡.**"
