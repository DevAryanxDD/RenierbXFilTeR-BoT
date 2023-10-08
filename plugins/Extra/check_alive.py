import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_photo(
        photo="https://telegra.ph/file/5b4335c589f685295ed17.jpg",
        caption="ɪ ᴀᴍ ᴀʟᴡᴀʏs ᴀʟɪᴠᴇ 🤖\n\n 🥀 ʜᴇʟʟᴏ, ᴛʜɪs ɪs <a href="https://t.me/RenierbXFilTeR_BoT">RᴇɴɪᴇʀʙX FɪʟTᴇR</a>\n⚙️ ᴀʟʟ sʏsᴛᴇᴍ ɪs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ\n👾 ʙᴏᴛ ᴠᴇʀsɪᴏɴ : 1.1.0 ʟᴀᴛᴇsᴛ\n🧑‍💻 ᴍʏ ᴍᴀsᴛᴇʀ <a href="https://t.me/itzRenierb">⋆‌⃝»‌𝐌ꝛ፝֟ 𝆺𝅥 ᭄𝗥ᴇɴɪᴇʀ𝗕ঔৣ ⍣⃟ ࿐</a>\n⚜️ ғᴜʟʟʏ ᴍᴏᴅɪғɪᴇᴅ ᴀɴᴅ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ\n♻️ ᴅᴀᴛᴀʙᴀsᴇ : <a href="www.mongodb.com">ᴍᴏɴɢᴏDB</a>\n\n❣️ ᴛʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ ❣️"
    )


@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("__**(❛ ᑭσɳց ❜!__**")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"__**꧁ Pong! ꧂__**\n\n   ⚘ {time_taken_s:.3f} ᴍs\n   ⚘ __**My**__ __**Master**__ <a href="https://t.me/itzRenierb">⋆‌⃝»‌𝐌ꝛ፝֟ 𝆺𝅥 ᭄𝗥ᴇɴɪᴇʀ𝗕ঔৣ ⍣⃟ ࿐</a>\n\n\n ᴍʏ ɴᴀᴍᴇ ɪs <a href="https://t.me/RenierbXFilTeR_BoT">RᴇɴɪᴇʀʙX FɪʟTᴇR</a> ᴛʜᴀɴᴋs <a href="https://t.me/RenierbXFilTeR_BoT">ᴍᴀsᴛᴇʀ</a> ᴛᴏ ᴅᴇᴠᴇʟᴏᴘ ᴍᴇ 💝💝 ")