notes_db = {}  # chat_id -> list

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def note(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if not context.args:
        await update.message.reply_text("Usage: /note <text>")
        return
    text = " ".join(context.args)
    notes_db.setdefault(chat_id, []).append(text)
    await update.message.reply_text(f"Note added: {text}")

async def list_notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    notes = notes_db.get(chat_id, [])
    if not notes:
        await update.message.reply_text("No notes.")
        return
    msg = "📋 *Your notes:*\n" + "\n".join(f"{i+1}. {n}" for i, n in enumerate(notes))
    await update.message.reply_text(msg, parse_mode='Markdown')

async def del_note(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if not context.args:
        await update.message.reply_text("Usage: /delnote <number>")
        return
    try:
        idx = int(context.args[0]) - 1
        notes = notes_db[chat_id]
        if 0 <= idx < len(notes):
            del notes[idx]
            await update.message.reply_text("Note deleted.")
        else:
            await update.message.reply_text("Invalid number.")
    except:
        await update.message.reply_text("Error.")

def register(app):
    app.add_handler(CommandHandler("note", note))
    app.add_handler(CommandHandler("notes", list_notes))
    app.add_handler(CommandHandler("delnote", del_note))