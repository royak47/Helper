from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

def help_command(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Ban User", callback_data="help_ban")],
        [InlineKeyboardButton("Mute User", callback_data="help_mute")],
        [InlineKeyboardButton("Filters", callback_data="help_filters")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Choose a command to learn more:", reply_markup=reply_markup)
    update.message.delete()

def help_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data

    if data == "help_ban":
        query.message.reply_text("Use /ban to ban a user. Reply to their message with this command.")
    elif data == "help_mute":
        query.message.reply_text("Use /mute to mute a user. Reply to their message with this command.")
    elif data == "help_filters":
        query.message.reply_text("Use /filter <keyword> <response> to set a filter.")
    query.answer()
