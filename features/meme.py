import requests
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def meme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    subreddits = ['memes', 'dankmemes', 'funny']
    try:
        r = requests.get(f"https://meme-api.com/gimme/{subreddits[__import__('random').randint(0,2)]}", timeout=10)
        data = r.json()
        await update.message.reply_photo(photo=data['url'])
    except:
        await update.message.reply_text("Meme nahi mila.")

def register(app):
    app.add_handler(CommandHandler("meme", meme))