from pyrogram.enums import ButtonStyle
from Oneforall.utils.inline.start import btn


class BUTTONS(object):

    MBUTTON = [

        # ================= ROW 1 =================

        [
            btn(
                "ᴄʜᴀᴛɢᴘᴛ 🤖",
                5222303112332598744,
                callback_data="mplus HELP_ChatGPT",
                style=ButtonStyle.PRIMARY,
            ),

            btn(
                "ʜɪsᴛᴏʀʏ 📜",
                5222305195391740380,
                callback_data="mplus HELP_History",
                style=ButtonStyle.SUCCESS,
            ),

            btn(
                "ʀᴇᴇʟ 🎬",
                5226526310725086929,
                callback_data="mplus HELP_Reel",
                style=ButtonStyle.PRIMARY,
            ),
        ],

        # ================= ROW 2 =================

        [
            btn(
                "ᴛᴀɢ-ᴀʟʟ📢",
                5226754927539287314,
                callback_data="mplus HELP_TagAll",
                style=ButtonStyle.DANGER,
            ),

            btn(
                "ɪɴғᴏℹ️",
                5228882959280401161,
                callback_data="mplus HELP_Info",
                style=ButtonStyle.SUCCESS,
            ),

            btn(
                "ᴇxᴛʀᴀ ⚙️",
                5220123403544980177,
                callback_data="mplus HELP_Extra",
                style=ButtonStyle.DANGER,
            ),
        ],

        # ================= ROW 3 =================

        [
            btn(
                "ᴄᴏᴜᴘʟᴇs 💕",
                5221961357489892670,
                callback_data="mplus HELP_Couples",
                style=ButtonStyle.PRIMARY,
            ),

            btn(
                "ᴀᴄᴛɪᴏɴ 🎭",
                5226934878079052543,
                callback_data="mplus HELP_Action",
                style=ButtonStyle.SUCCESS,
            ),

            btn(
                "sᴇᴀʀᴄʜ 🔎",
                5229057012830071691,
                callback_data="mplus HELP_Search",
                style=ButtonStyle.PRIMARY,
            ),
        ],

        # ================= ROW 4 =================

        [
            btn(
                "ғᴏɴᴛ 🔤",
                5226936291123295076,
                callback_data="mplus HELP_Font",
                style=ButtonStyle.DANGER,
            ),

            btn(
                "ʙᴏᴛs 🤖",
                5222379030174526318,
                callback_data="mplus HELP_Bots",
                style=ButtonStyle.PRIMARY,
            ),

            btn(
                "ᴛ-ɢʀᴀᴘʜ 📊",
                5229197127548170112,
                callback_data="mplus HELP_TG",
                style=ButtonStyle.DANGER,
            ),
        ],

        # ================= ROW 5 =================

        [
            btn(
                "sᴏᴜʀᴄᴇ 📂",
                5228904829253869947,
                callback_data="mplus HELP_Source",
                style=ButtonStyle.PRIMARY,
            ),

            btn(
                "ᴛʀᴜᴛʜ-ᴅᴀʀᴇ ⚖️",
                5222121319251860086,
                callback_data="mplus HELP_TD",
                style=ButtonStyle.SUCCESS,
            ),

            btn(
                "ǫᴜɪᴢ 🧩",
                5228934185355338030,
                callback_data="mplus HELP_Quiz",
                style=ButtonStyle.PRIMARY,
            ),
        ],

        # ================= ROW 6 =================

        [
            btn(
                "ᴛᴛs 🗣️",
                5226839516920181422,
                callback_data="mplus HELP_TTS",
                style=ButtonStyle.DANGER,
            ),

            btn(
                "ʀᴀᴅɪᴏ 📻",
                5226534191990074874,
                callback_data="mplus HELP_Radio",
                style=ButtonStyle.PRIMARY,
            ),

            btn(
                "ǫᴜᴏᴛʟʏ 📝",
                5208726716414981909,
                callback_data="mplus HELP_Q",
                style=ButtonStyle.DANGER,
            ),
        ],

        # ================= POWERED =================

        [
            btn(
                "✨ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʀᴏᴏʜɪ ✨",
                5226938803679162970,
                url="https://t.me/Go_And_Love_Yourself_Brother",
                style=ButtonStyle.SUCCESS,
            ),
        ],

                    # ================= ================= NAVIGATION =================

[
btn(
"ʙᴀᴄᴋ",
5462931610028510371,
callback_data="settings_back_helper",
style=ButtonStyle.PRIMARY
),

btn(  
    "ʜᴏᴍᴇ",  
    5796647601105276281,  
    callback_data="settingsback_helper",  
    style=ButtonStyle.SUCCESS  
),  

btn(  
    "ɴᴇxᴛ",  
    5465144931230190889,  
    callback_data="managebot123 settings_back_helper",  
    style=ButtonStyle.PRIMARY  
),

],

            # ================= CLOSE =================

        [
            btn(
                "ᴄʟᴏsᴇ",
                5210952531676504517,
                callback_data="close",
                style=ButtonStyle.DANGER
            ),
        ],

    ]