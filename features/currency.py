import os
import requests
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

API_KEY = os.environ.get("EXCHANGE_API_KEY")

async def convert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 3:
        await update.message.reply_text("Usage: /convert <amount> <from_currency> <to_currency>\nExample: /convert 100 USD INR")
        return
    amount, from_cur, to_cur = context.args
    if not API_KEY:
        await update.message.reply_text("Exchange API key missing.")
        return
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{from_cur}/{to_cur}"
    try:
        r = requests.get(url)
        data = r.json()
        rate = data['conversion_rate']
        result = float(amount) * rate
        await update.message.reply_text(f"💱 {amount} {from_cur} = {result:.2f} {to_cur}")
    except:
        await update.message.reply_text("Conversion failed.")

def register(app):
    app.add_handler(CommandHandler("convert", convert))