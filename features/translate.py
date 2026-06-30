from translate import Translator
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def translate_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("Usage: /tr <target_lang> <text>\nExample: /tr es Hello world")
        return
    lang = context.args[0]
    text = " ".join(context.args[1:])
    try:
        translator = Translator(to_lang=lang)
        translation = translator.translate(text)
        await update.message.reply_text(f"🌐 *{lang}*: {translation}", parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text("Translation failed. Invalid language code?")

def register(app):
    app.add_handler(CommandHandler("tr", translate_cmd))