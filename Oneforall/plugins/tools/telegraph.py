import os
import requests

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Oneforall import app


def upload_file(file_path):

    server = requests.get(
        "https://api.gofile.io/servers"
    ).json()["data"]["servers"][0]["name"]

    with open(file_path, "rb") as f:

        response = requests.post(
            f"https://{server}.gofile.io/uploadFile",
            files={"file": f}
        )

    data = response.json()

    if data["status"] == "ok":
        return True, data["data"]["downloadPage"]

    return False, "Upload failed"

@app.on_message(
    filters.command(
        ["tgm", "tgt", "telegraph", "tl"]
    )
)
async def telegraph_upload(client, message):

    if not message.reply_to_message:

        return await message.reply_text(
            "❌ Reply to a media file."
        )

    media = message.reply_to_message

    if not (
        media.photo
        or media.video
        or media.document
        or media.audio
    ):

        return await message.reply_text(
            "❌ Unsupported media."
        )

    text = await message.reply_text(
        "📥 Downloading..."
    )

    try:

        file_path = await media.download()

        await text.edit_text(
            "📤 Uploading to Catbox..."
        )

        success, result = upload_file(file_path)

        if success:

            buttons = InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "🌐 Open Link",
                        url=result
                    )
                ]]
            )

            await text.edit_text(
                f"✅ Uploaded Successfully\n\n{result}",
                reply_markup=buttons,
                disable_web_page_preview=True
            )

        else:

            await text.edit_text(
                f"❌ Upload Failed\n\n`{result}`"
            )

        try:
            os.remove(file_path)
        except:
            pass

    except Exception as e:

        await text.edit_text(
            f"❌ Error:\n`{e}`"
        )

__HELP__ = """
**ᴛᴇʟᴇɢʀᴀᴘʜ ᴜᴘʟᴏᴀᴅ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs**

ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴍᴇᴅɪᴀ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ:

- `/tgm`: ᴜᴘʟᴏᴀᴅ ʀᴇᴘʟɪᴇᴅ ᴍᴇᴅɪᴀ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ.
- `/tgt`: sᴀᴍᴇ ᴀs `/tgm`.
- `/telegraph`: sᴀᴍᴇ ᴀs `/tgm`.
- `/tl`: sᴀᴍᴇ ᴀs `/tgm`.

**ᴇxᴀᴍᴘʟᴇ:**
- ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ᴠɪᴅᴇᴏ ᴡɪᴛʜ `/tgm` ᴛᴏ ᴜᴘʟᴏᴀᴅ ɪᴛ.

**ɴᴏᴛᴇ:**
ʏᴏᴜ ᴍᴜsᴛ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇᴅɪᴀ ғɪʟᴇ ғᴏʀ ᴛʜᴇ ᴜᴘʟᴏᴀᴅ ᴛᴏ ᴡᴏʀᴋ.
"""

__MODULE__ = "Tᴇʟᴇɢʀᴀᴘʜ"
