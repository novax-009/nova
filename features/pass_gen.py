import random
import string
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def passgen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    length = 12
    if context.args:
        try:
            length = int(context.args[0])
        except:
            pass
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(length))
    await update.message.reply_text(f"🔐 `{password}`", parse_mode='MarkdownV2')

def register(app):
    app.add_handler(CommandHandler("passgen", passgen))