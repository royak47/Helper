from telegram import Update
from telegram.ext import CallbackContext

def start_command(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! Welcome to the bot. Use /help to see what I can do.")
    update.message.delete()
