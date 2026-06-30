import os
import requests
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

API_KEY = os.environ.get("NEWS_API_KEY")

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not API_KEY:
        await update.message.reply_text("News API key set nahi hai.")
        return
    query = " ".join(context.args) if context.args else "India"
    url = f"https://newsapi.org/v2/top-headlines?q={query}&apiKey={API_KEY}&pageSize=5"
    try:
        r = requests.get(url)
        data = r.json()
        if data.get("status") != "ok":
            await update.message.reply_text("News fetch nahi ho paayi.")
            return
        articles = data.get("articles", [])
        if not articles:
            await update.message.reply_text("Koi news nahi mili.")
            return
        msg = "📰 *Top Headlines:*\n"
        for i, art in enumerate(articles[:5], 1):
            title = art['title']
            msg += f"{i}. [{title}]({art['url']})\n"
        await update.message.reply_text(msg, parse_mode='Markdown', disable_web_page_preview=True)
    except Exception as e:
        await update.message.reply_text("Error fetching news.")

def register(app):
    app.add_handler(CommandHandler("news", news))