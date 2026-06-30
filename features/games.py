import random
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dice = random.randint(1, 6)
    await update.message.reply_text(f"🎲 You rolled: {dice}")

def register(app):
    app.add_handler(CommandHandler("roll", roll))  
    
# games.py ke andar ye extra code (can be separate file or same)
import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackQueryHandler, CommandHandler, ContextTypes

games = {}  # chat_id -> board

async def tictactoe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    board = [" "]*9
    games[chat_id] = board
    await update.message.reply_text("Tic Tac Toe! You are X", reply_markup=build_keyboard(board))

def build_keyboard(board):
    keyboard = []
    for i in range(0, 9, 3):
        row = [InlineKeyboardButton(board[j] if board[j]!=" " else "▫️", callback_data=f"ttt_{j}") for j in range(i, i+3)]
        keyboard.append(row)
    return InlineKeyboardMarkup(keyboard)

async def ttt_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    chat_id = query.message.chat_id
    if data.startswith("ttt_"):
        idx = int(data.split("_")[1])
        board = games.get(chat_id)
        if not board:
            await query.edit_message_text("Game expired.")
            return
        if board[idx] != " ":
            return
        board[idx] = "X"
        if check_win(board, "X"):
            await query.edit_message_text("You win! 🎉")
            del games[chat_id]
            return
        # simple bot move: random empty
        empty = [i for i, v in enumerate(board) if v==" "]
        if not empty:
            await query.edit_message_text("It's a draw!")
            del games[chat_id]
            return
        bot_idx = random.choice(empty)
        board[bot_idx] = "O"
        if check_win(board, "O"):
            await query.edit_message_text("Bot wins! 🤖")
            del games[chat_id]
            return
        await query.edit_message_text("Your turn (X)", reply_markup=build_keyboard(board))

def check_win(b, p):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[a]==b[b_]==b[c]==p for a,b_,c in wins)

def register(app):
    app.add_handler(CommandHandler("roll", roll))
    app.add_handler(CommandHandler("ttt", tictactoe))
    app.add_handler(CallbackQueryHandler(ttt_callback, pattern="ttt_"))