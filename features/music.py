import requests
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

HF_SPACE_URL = "https://novax-009-novax.hf.space"

async def dl(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = " ".join(context.args)
    if not url:
        await update.message.reply_text("🎵 *Usage:* `/dl <youtube_url>`", parse_mode="Markdown")
        return
    
    if "youtube.com" not in url and "youtu.be" not in url:
        await update.message.reply_text("❌ Please provide a valid YouTube URL.")
        return
    
    msg = await update.message.reply_text("⏳ Downloading audio... Please wait.")
    
    try:
        api = f"{HF_SPACE_URL}/download?url={url}"
        response = requests.get(api, timeout=120)
        
        if response.status_code == 200:
            await msg.delete()
            await update.message.reply_audio(
                audio=response.content,
                title="NovaX Music 🎵",
                performer="Downloaded by NovaX Bot",
                caption="🎧 Enjoy your music!\nPowered by NovaX"
            )
        else:
            await msg.edit_text(f"❌ Download failed. The video might be too long or unavailable.\n\nTry another URL.")
    
    except requests.exceptions.Timeout:
        await msg.edit_text("⏰ Request timed out. The song might be too long. Try a shorter video (under 5 minutes).")
    
    except Exception as e:
        await msg.edit_text(f"❌ Error: Something went wrong.\nTry again later.")

async def song_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "🎵 *NovaX Music Downloader*\n\n"
        "*Commands:*\n"
        "`/dl <youtube_url>` – Download MP3 from YouTube\n"
        "`/musichelp` – This help message\n\n"
        "*How to use:*\n"
        "1. Copy YouTube video URL\n"
        "2. Send `/dl <paste_url>`\n"
        "3. Wait for audio file\n\n"
        "*Tips:*\n"
        "• Videos under 5 minutes work best\n"
        "• First request may take 30-60 seconds\n"
        "• Audio quality: 128kbps MP3"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")

def register(app):
    app.add_handler(CommandHandler("dl", dl))
    app.add_handler(CommandHandler("musichelp", song_help))
