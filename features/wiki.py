from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
import wikipedia
wikipedia.set_lang("en")

async def wiki(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args)
    if not query:
        await update.message.reply_text("Usage: /wiki <topic>")
        return
    try:
        summary = wikipedia.summary(query, sentences=3)
        await update.message.reply_text(f"📖 *{query}*\n{summary}", parse_mode='Markdown')
    except wikipedia.exceptions.DisambiguationError as e:
        await update.message.reply_text(f"Multiple options: {', '.join(e.options[:5])}")
    except wikipedia.exceptions.PageError:
        await update.message.reply_text("Page not found.")

def register(app):
    app.add_handler(CommandHandler("wiki", wiki))