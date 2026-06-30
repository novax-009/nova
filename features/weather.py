import os
import requests
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

API_KEY = os.environ.get("WEATHER_API_KEY")

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not API_KEY:
        await update.message.reply_text("Weather API key set nahi hai.")
        return
    city = " ".join(context.args) if context.args else "Delhi"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        if r.status_code != 200:
            await update.message.reply_text(f"City nahi mili: {data.get('message', 'Unknown error')}")
            return
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        await update.message.reply_text(f"🌤 {city.capitalize()}: {temp}°C, {desc}")
    except Exception as e:
        await update.message.reply_text("Weather fetch karne mein error.")

def register(app):
    app.add_handler(CommandHandler("weather", weather))