import asyncio
from datetime import datetime
import dateparser
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def remind(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args or len(context.args) < 2:
        await update.message.reply_text("Format: /remind <time> <message>\nExample: /remind 10m chai pee lo")
        return
    time_str = context.args[0]
    msg = " ".join(context.args[1:])
    now = datetime.now()
    when = dateparser.parse(time_str, settings={'PREFER_DATES_FROM': 'future'})
    if not when:
        await update.message.reply_text("Time samajh nahi aaya. Please try again.")
        return
    diff = (when - now).total_seconds()
    if diff <= 0:
        await update.message.reply_text("Ye time past mein hai.")
        return
    await update.message.reply_text(f"⏰ Reminder set for {when.strftime('%Y-%m-%d %H:%M')}.")
    await asyncio.sleep(diff)
    await update.message.reply_text(f"⏰ Reminder: {msg}")

def register(app):
    app.add_handler(CommandHandler("remind", remind))