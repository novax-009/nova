import requests
import yfinance as yf
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def crypto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coin = " ".join(context.args).lower()
    if not coin:
        await update.message.reply_text("Usage: /crypto bitcoin")
        return
    try:
        r = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd")
        data = r.json()
        if coin in data:
            price = data[coin]['usd']
            await update.message.reply_text(f"💰 {coin.capitalize()}: ${price}")
        else:
            await update.message.reply_text("Coin not found.")
    except:
        await update.message.reply_text("Error.")

async def stock(update: Update, context: ContextTypes.DEFAULT_TYPE):
    symbol = " ".join(context.args).upper()
    if not symbol:
        await update.message.reply_text("Usage: /stock RELIANCE.NS (for NSE) or AAPL")
        return
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        price = info.get('regularMarketPrice') or info.get('currentPrice')
        await update.message.reply_text(f"📈 {symbol}: ₹{price}" if '.NS' in symbol else f"📈 {symbol}: ${price}")
    except:
        await update.message.reply_text("Error fetching stock price.")

def register(app):
    app.add_handler(CommandHandler("crypto", crypto))
    app.add_handler(CommandHandler("stock", stock))