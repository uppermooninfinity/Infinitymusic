from pyrogram import filters
from pymongo import MongoClient
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Oneforall import app
import random

MONGO_DB_URI = "mongodb+srv://I-LOVE-PDF-BOT:I-LOVE-PDF-BOT@cluster0.c51o3a9.mongodb.net/?retryWrites=true&w=majority"

mongo_client = MongoClient(MONGO_DB_URI)

db = mongo_client["natu_rankings"]
collection = db["ranking"]

user_data = {}
today = {}

MISHI = [
    "https://telegra.ph/file/a6a5b78007e4ca766794a.jpg",
]


# WATCHER
@app.on_message(filters.group, group=6)
async def today_watcher(_, message):

    if not message.from_user:
        return

    chat_id = message.chat.id
    user_id = message.from_user.id

    if chat_id not in today:
        today[chat_id] = {}

    if user_id not in today[chat_id]:
        today[chat_id][user_id] = {"total_messages": 0}

    today[chat_id][user_id]["total_messages"] += 1


@app.on_message(filters.group, group=11)
async def overall_watcher(_, message):

    if not message.from_user:
        return

    user_id = message.from_user.id

    user_data.setdefault(user_id, {})
    user_data[user_id].setdefault("total_messages", 0)

    user_data[user_id]["total_messages"] += 1

    collection.update_one(
        {"_id": user_id},
        {"$inc": {"total_messages": 1}},
        upsert=True
    )


# FORMAT USER
async def format_user(user_id, total_messages, index):

    try:
        user = await app.get_users(user_id)

        first_name = user.first_name or "User"

        mention = f"[{first_name}](tg://user?id={user_id})"

    except:
        mention = "Unknown User"

    medals = {
        1: "🥇",
        2: "🥈",
        3: "🥉"
    }

    medal = medals.get(index, "✨")

    return (
        f"{medal} {index}. {mention}\n"
        f"   ┗ 💬 Messages: `{total_messages}`\n\n"
    )


# TODAY RANK
@app.on_message(filters.command("today"))
async def today_rank(_, message):

    chat_id = message.chat.id

    if chat_id not in today:
        return await message.reply_text(
            "❌ No data available for today."
        )

    users_data = [
        (user_id, data["total_messages"])
        for user_id, data in today[chat_id].items()
    ]

    sorted_users = sorted(
        users_data,
        key=lambda x: x[1],
        reverse=True
    )[:10]

    if not sorted_users:
        return await message.reply_text(
            "❌ No rankings found."
        )

    total_messages = sum(
        data["total_messages"]
        for data in today[chat_id].values()
    )

    caption = (
        "🏆 **TODAY LEADERBOARD** 🏆\n\n"
        f"💬 Total Messages: `{total_messages}`\n\n"
    )

    for idx, (user_id, msgs) in enumerate(sorted_users, start=1):
        caption += await format_user(user_id, msgs, idx)

    buttons = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(
                "🌍 Overall Leaderboard",
                callback_data="overall"
            )
        ]]
    )

    await message.reply_photo(
        photo=random.choice(MISHI),
        caption=caption,
        reply_markup=buttons
    )


# OVERALL RANK
@app.on_message(filters.command("ranking"))
async def overall_rank_cmd(_, message):

    top_members = collection.find().sort(
        "total_messages",
        -1
    ).limit(10)

    caption = "🏆 **OVERALL LEADERBOARD** 🏆\n\n"

    for idx, member in enumerate(top_members, start=1):

        user_id = member["_id"]
        total_messages = member["total_messages"]

        caption += await format_user(
            user_id,
            total_messages,
            idx
        )

    buttons = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(
                "📅 Today Leaderboard",
                callback_data="today"
            )
        ]]
    )

    await message.reply_photo(
        photo=random.choice(MISHI),
        caption=caption,
        reply_markup=buttons
    )


# TODAY CALLBACK
@app.on_callback_query(filters.regex("^today$"))
async def today_callback(_, query):

    chat_id = query.message.chat.id

    if chat_id not in today:
        return await query.answer(
            "No data available.",
            show_alert=True
        )

    users_data = [
        (user_id, data["total_messages"])
        for user_id, data in today[chat_id].items()
    ]

    sorted_users = sorted(
        users_data,
        key=lambda x: x[1],
        reverse=True
    )[:10]

    caption = "🏆 **TODAY LEADERBOARD** 🏆\n\n"

    for idx, (user_id, msgs) in enumerate(sorted_users, start=1):
        caption += await format_user(user_id, msgs, idx)

    buttons = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(
                "🌍 Overall Leaderboard",
                callback_data="overall"
            )
        ]]
    )

    try:
        await query.message.edit_caption(
            caption=caption,
            reply_markup=buttons
        )
    except:
        pass


# OVERALL CALLBACK
@app.on_callback_query(filters.regex("^overall$"))
async def overall_callback(_, query):

    top_members = collection.find().sort(
        "total_messages",
        -1
    ).limit(10)

    caption = "🏆 **OVERALL LEADERBOARD** 🏆\n\n"

    for idx, member in enumerate(top_members, start=1):

        user_id = member["_id"]
        total_messages = member["total_messages"]

        caption += await format_user(
            user_id,
            total_messages,
            idx
        )

    buttons = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(
                "📅 Today Leaderboard",
                callback_data="today"
            )
        ]]
    )

    try:
        await query.message.edit_caption(
            caption=caption,
            reply_markup=buttons
        )
    except:
        pass