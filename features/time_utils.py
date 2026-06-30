from datetime import datetime
import pytz
from dateutil.relativedelta import relativedelta
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def time_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = " ".join(context.args) if context.args else "UTC"
    try:
        tz = pytz.timezone(city)
    except pytz.UnknownTimeZoneError:
        await update.message.reply_text("Invalid timezone. Example: /time Asia/Kolkata")
        return
    now = datetime.now(tz)
    await update.message.reply_text(f"🕒 {city}: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}")

async def age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /age YYYY-MM-DD")
        return
    dob_str = context.args[0]
    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
    except:
        await update.message.reply_text("Format: YYYY-MM-DD")
        return
    now = datetime.now()
    diff = relativedelta(now, dob)
    await update.message.reply_text(f"🎂 Age: {diff.years} years, {diff.months} months, {diff.days} days")

def register(app):
    app.add_handler(CommandHandler("time", time_cmd))
    app.add_handler(CommandHandler("age", age))