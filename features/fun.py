import random
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

JOKES = [
    "Teacher: \"Baccho, aaj hum English mein baat karenge.\"\nPappu: \"Sir, pen nahi laya, pencil se likh loon?\"",
    "Wife: \"Suno ji, aaj maine aapki favourite dish banayi hai.\"\nHusband: \"Accha, toh tumne Maggi banayi?\"",
    "Ek aadmi ne doosre se kaha: \"Tum itne thande kyun ho?\"\nDoosra bola: \"Mera dil fridge mein hai.\""
]

FACTS = [
    "Octopus ke 3 dil hote hain.",
    "Shahad kabhi kharab nahi hota.",
    "Banana technically ek berry hai.",
    "Aap apni kohni nahi chaat sakte (99% log try karte hain)."
]

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"😹 *Joke Time!*\n{random.choice(JOKES)}", parse_mode='Markdown')

async def fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🧠 *Did You Know?*\n{random.choice(FACTS)}", parse_mode='Markdown')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)
    if text:
        await update.message.reply_text(f"🔁 {text}")
    else:
        await update.message.reply_text("Kuch text bhi do echo karne ke liye, jaise /echo Hello")

def register(application):
    application.add_handler(CommandHandler("joke", joke))
    application.add_handler(CommandHandler("fact", fact))
    application.add_handler(CommandHandler("echo", echo))