from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Pong! NovaX is up and running.")

def register(application):
    application.add_handler(CommandHandler("ping", ping))