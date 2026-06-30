import io
from PIL import Image
from telegram import Update
from telegram.ext import MessageHandler, filters, ContextTypes

async def convert_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.document.get_file()
    if not file:
        return
    # download
    bytes = await file.download_as_bytearray()
    im = Image.open(io.BytesIO(bytes))
    # PNG me convert karein
    out = io.BytesIO()
    im.save(out, format='PNG')
    out.seek(0)
    await update.message.reply_document(document=out, filename="converted.png")

def register(app):
    app.add_handler(MessageHandler(filters.Document.IMAGE, convert_image))