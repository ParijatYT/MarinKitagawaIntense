import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EmikoRobot.events import register
from EmikoRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/4a364b20fafb4b3ee65db.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**𝙃𝙞 [{event.sender.first_name}](tg://user?id={event.sender.id}), 𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙣 𝙆𝙞𝙩𝙖𝙜𝙖𝙬𝙖.** \n\n"
    TEXT += "✧ **𝙄 𝙖𝙢 𝘼𝙡𝙞𝙫𝙚 𝙖𝙣𝙙 𝙄𝙣𝙩𝙚𝙣𝙨𝙚** \n\n"
    TEXT += (
        f"✧ **𝙅𝙤𝙞𝙣 𝙈𝙮 𝙉𝙚𝙩𝙬𝙤𝙧𝙠 : [𝙄𝙣𝙩𝙚𝙣𝙨𝙚 𝙉𝙚𝙩𝙬𝙤𝙧𝙠](https://t.me/IntenseNetwork)** \n\n"
    )
    TEXT += f"✧ **𝙇𝙞𝙗𝙧𝙖𝙧𝙮 𝙑𝙚𝙧𝙨𝙞𝙤𝙣 :** `{telever}` \n\n"
    TEXT += f"✧ **𝙏𝙚𝙡𝙚𝙩𝙝𝙤𝙣 𝙑𝙚𝙧𝙨𝙞𝙤𝙣 :** `{tlhver}` \n\n"
    TEXT += f"✧ **𝙋𝙮𝙧𝙤𝙜𝙧𝙖𝙢 𝙑𝙚𝙧𝙨𝙞𝙤𝙣 :** `{pyrover}` \n\n"
    TEXT += "**𝙏𝙝𝙖𝙣𝙠𝙨 𝙁𝙤𝙧 𝘼𝙙𝙙𝙞𝙣𝙜 𝙈𝙚 𝙃𝙚𝙧𝙚...**"
    BUTTON = [
        [
            Button.url("𝙃𝙚𝙡𝙥", "https://t.me/MarinKitagawa_IntenseBot?start=help"),
            Button.url("𝙎𝙪𝙥𝙥𝙤𝙧𝙩", "https://t.me/MarinKitagawaIntenseSupport"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
