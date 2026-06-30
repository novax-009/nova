import os
import requests
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

TOKEN = os.environ.get("BITLY_TOKEN")

async def short(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = " ".join(context.args)
    if not url:
        await update.message.reply_text("Usage: /short https://example.com")
        return
    if not TOKEN:
        await update.message.reply_text("Bitly token missing.")
        return
    headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
    data = {"long_url": url}
    try:
        r = requests.post("https://api-ssl.bitly.com/v4/shorten", json=data, headers=headers)
        resp = r.json()
        if 'link' in resp:
            await update.message.reply_text(f"🔗 {resp['link']}")
        else:
            await update.message.reply_text("Could not shorten.")
    except:
        await update.message.reply_text("Error.")

def register(app):
    app.add_handler(CommandHandler("short", short))