import requests
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        r = requests.get("https://api.quotable.io/random", timeout=10)
        data = r.json()
        text = f"💬 *{data['content']}*\n― {data['author']}"
        await update.message.reply_text(text, parse_mode='Markdown')
    except:
        await update.message.reply_text("Quote nahi mila.")

def register(app):
    app.add_handler(CommandHandler("quote", quote))