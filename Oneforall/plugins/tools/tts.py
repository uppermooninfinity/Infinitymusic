import io
from gtts import gTTS
from pyrogram import filters

from Oneforall import app


VOICES = {
    "girl": {
        "lang": "en",
        "tld": "co.in"
    },
    "boy": {
        "lang": "en",
        "tld": "com.au"
    },
    "robot": {
        "lang": "en",
        "tld": "us"
    },
    "hindi": {
        "lang": "hi",
        "tld": "co.in"
    }
}


@app.on_message(filters.command("tts"))
async def text_to_speech(client, message):

    if len(message.command) < 3:

        return await message.reply_text(
            "**Usage:**\n\n"
            "`/tts girl Hello`\n"
            "`/tts boy Hello`\n"
            "`/tts robot Hello`\n"
            "`/tts hindi Namaste`\n"
        )

    try:

        args = message.text.split(maxsplit=2)

        voice = args[1].lower()
        text = args[2]

        if voice not in VOICES:

            return await message.reply_text(
                "❌ Available voices:\n"
                "`girl`\n"
                "`boy`\n"
                "`robot`\n"
                "`hindi`"
            )

        status = await message.reply_text(
            "🎤 Generating AI Voice..."
        )

        settings = VOICES[voice]

        tts = gTTS(
            text=text,
            lang=settings["lang"],
            tld=settings["tld"],
            slow=False
        )

        audio_data = io.BytesIO()

        tts.write_to_fp(audio_data)

        audio_data.seek(0)

        audio_file = io.BytesIO(
            audio_data.read()
        )

        audio_file.name = "tts.mp3"

        await message.reply_audio(
            audio=audio_file,
            title=f"{voice.title()} AI Voice",
            performer="Oneforall AI"
        )

        await status.delete()

    except Exception as e:

        await message.reply_text(
            f"❌ Error:\n`{e}`"
        )


__HELP__ = """
/tts girl Hello Baby
/tts boy Hello Bro
/tts robot System Activated
/tts hindi Namaste Duniya
"""

__MODULE__ = "AI-TTS"