import requests
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        r = requests.get("https://official-joke-api.appspot.com/random_joke", timeout=10)
        data = r.json()
        text = f"😂 {data['setup']}\n\n{data['punchline']}"
        await update.message.reply_text(text)
    except:
        await update.message.reply_text("Joke fetch nahi ho paaya.")

def register(app):
    app.add_handler(CommandHandler("joke", joke))