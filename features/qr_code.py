import io
import qrcode
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def qr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)
    if not text:
        await update.message.reply_text("Usage: /qr <text or URL>")
        return
    img = qrcode.make(text)
    bio = io.BytesIO()
    img.save(bio, format='PNG')
    bio.seek(0)
    await update.message.reply_photo(photo=bio)

def register(app):
    app.add_handler(CommandHandler("qr", qr))