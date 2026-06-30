from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⚡ Commands", callback_data='help')],
        [InlineKeyboardButton("🧩 Fun", callback_data='fun')],
        [InlineKeyboardButton("ℹ️ About", callback_data='about')],
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👾 *NovaX* – The Ultimate Multi‑Action Bot\n"
        "──────────────────────\n"
        "Main aapka AI buddy jo weather, news, calculator, reminders, aur bahut kuch kar sakta hai.\n"
        "Neeche button dabao ya command type karo!",
        reply_markup=markup,
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🌟 *Available Commands:*\n"
        "/start – Welcome message\n"
        "/help – Yeh list\n"
        "/ping – Bot alive check\n"
        "/joke – Random joke\n"
        "/fact – Random fact\n"
        "/echo <text> – Echo karega\n"
        "/about – Bot ke baare mein"
    )
    await update.message.reply_text(text, parse_mode='Markdown')

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *NovaX Bot*\n"
        "Version 1.0 – Multi‑Action Legend\n"
        "Created with ❤️ by [Your Name]",
        parse_mode='Markdown'
    )

def register(application):
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about))