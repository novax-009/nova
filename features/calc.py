from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from simpleeval import simple_eval

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    expr = " ".join(context.args)
    if not expr:
        await update.message.reply_text("Expression do, jaise /calc 2+3*4")
        return
    try:
        result = simple_eval(expr)
        await update.message.reply_text(f"🔢 {expr} = {result}")
    except Exception:
        await update.message.reply_text("Invalid expression. Try again.")

def register(app):
    app.add_handler(CommandHandler("calc", calc))