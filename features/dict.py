import requests
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def define(update: Update, context: ContextTypes.DEFAULT_TYPE):
    word = " ".join(context.args)
    if not word:
        await update.message.reply_text("Usage: /define <word>")
        return
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        r = requests.get(url)
        if r.status_code != 200:
            await update.message.reply_text("Word not found.")
            return
        data = r.json()[0]
        meaning = data['meanings'][0]['definitions'][0]['definition']
        await update.message.reply_text(f"📘 *{word}*: {meaning}", parse_mode='Markdown')
    except:
        await update.message.reply_text("Error fetching definition.")

def register(app):
    app.add_handler(CommandHandler("define", define))