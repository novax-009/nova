import requests
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def lyrics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("Usage: /lyrics <artist> <song>")
        return
    artist, song = context.args[0], " ".join(context.args[1:])
    try:
        r = requests.get(f"https://api.lyrics.ovh/v1/{artist}/{song}")
        if r.status_code == 200:
            data = r.json()
            text = data['lyrics'][:1500]  # Telegram message limit
            await update.message.reply_text(f"🎵 *{artist} - {song}*\n{text}", parse_mode='Markdown')
        else:
            await update.message.reply_text("Lyrics not found.")
    except:
        await update.message.reply_text("Error.")

def register(app):
    app.add_handler(CommandHandler("lyrics", lyrics))