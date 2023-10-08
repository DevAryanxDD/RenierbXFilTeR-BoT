# Renierb X - Telegram Projects
# (c) 2023 - 2024 Renierb

from pyrogram import Client, filters
from utils import temp
from pyrogram.types import Message
from database.users_chats_db import db
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import SUPPORT_CHAT

async def banned_users(_, client, message: Message):
    return (
        message.from_user is not None or not message.sender_chat
    ) and message.from_user.id in temp.BANNED_USERS

banned_user = filters.create(banned_users)

async def disabled_chat(_, client, message: Message):
    return message.chat.id in temp.BANNED_CHATS

disabled_group=filters.create(disabled_chat)


@Client.on_message(filters.private & banned_user & filters.incoming)
async def ban_reply(bot, message):
    buttons = [[
        InlineKeyboardButton('♻️ ꜱᴜᴘᴘᴏʀᴛ ♻️', url=f'https://t.me/{SUPPORT_CHAT}')
    ]]
    reply_markup=InlineKeyboardMarkup(buttons)
    ban = await db.get_ban_status(message.from_user.id)
    await message.reply(f'ꜱᴏʀʀʏ ᴅᴜᴅᴇ ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜꜱᴇ ᴍᴇ \n\nʙᴀɴ ʀᴇᴀꜱᴏɴ: {ban["ban_reason"]}\n\nɪғ ᴛʜɪꜱ ɪꜱ ᴀ ᴍɪꜱᴛᴀᴋᴇ ᴘʟᴇᴀꜱᴇ ʀᴇᴀᴄʜ ᴏᴜᴛ ᴛᴏ ᴏᴜʀ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ')

@Client.on_message(filters.group & disabled_group & filters.incoming)
async def grp_bd(bot, message):
    buttons = [[
        InlineKeyboardButton('♻️ ꜱᴜᴘᴘᴏʀᴛ ♻️', url=f'https://t.me/{SUPPORT_CHAT}')
    ]]
    reply_markup=InlineKeyboardMarkup(buttons)
    vazha = await db.get_chat(message.chat.id)
    k = await message.reply(
        text=f"‼️ 𝗖𝗛𝗔𝗧 𝗡𝗢𝗧 𝗔𝗟𝗟𝗢𝗪𝗘𝗗 ‼️\n\nᴍʏ ᴀᴅᴍɪɴꜱ ʜᴀᴠᴇ ʀᴇꜱᴛʀɪᴄᴛᴇᴅ ᴍᴇ ғʀᴏᴍ ᴡᴏʀᴋɪɴɢ ʜᴇʀᴇ !! ᴋɪɴᴅʟʏ ʀᴇᴀᴄʜ ᴏᴜᴛ ᴛᴏ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ғᴏʀ ᴀɴʏ ǫᴜᴇʀɪᴇꜱ.\n\n♻️ ʀᴇɢᴀʀᴅꜱ :<a href=https://t.me/TeamRenierb> Tᴇᴀᴍ Rᴇɴɪᴇʀʙ </a>\nReason : <code>{vazha['reason']}</code>.",
        reply_markup=reply_markup)
    try:
        await k.pin()
    except:
        pass
    await bot.leave_chat(message.chat.id)
