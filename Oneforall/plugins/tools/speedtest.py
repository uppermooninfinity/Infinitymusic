import asyncio
import speedtest

from pyrogram import filters
from pyrogram.types import Message

from Oneforall import app
from Oneforall.misc import SUDOERS


def run_speedtest():

    test = speedtest.Speedtest()

    test.get_best_server()

    test.download()
    test.upload()

    test.results.share()

    return test.results.dict()


@app.on_message(filters.command(["speedtest", "spt"]) & SUDOERS)
async def speedtest_function(client, message: Message):

    m = await message.reply_text(
        "⚡ **Running Speed Test...**"
    )

    try:

        loop = asyncio.get_event_loop()

        result = await loop.run_in_executor(
            None,
            run_speedtest
        )

        download = round(
            result["download"] / 1024 / 1024,
            2
        )

        upload = round(
            result["upload"] / 1024 / 1024,
            2
        )

        ping = result["ping"]

        isp = result["client"]["isp"]

        country = result["client"]["country"]

        server = result["server"]["name"]

        sponsor = result["server"]["sponsor"]

        latency = result["server"]["latency"]

        caption = f"""
🏆 **SPEED TEST RESULT**

📥 **Download:** `{download} Mbps`
📤 **Upload:** `{upload} Mbps`
📡 **Ping:** `{ping} ms`

🌍 **ISP:** `{isp}`
🇮🇳 **Country:** `{country}`

🖥 **Server:** `{server}`
🏢 **Sponsor:** `{sponsor}`
⚡ **Latency:** `{latency}`
"""

        await message.reply_photo(
            photo=result["share"],
            caption=caption
        )

        await m.delete()

    except Exception as e:

        await m.edit_text(
            f"❌ Error:\n`{e}`"
        )