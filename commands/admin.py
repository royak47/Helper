from telegram import Update
from telegram.ext import CallbackContext
from telegram.error import BadRequest

def ban_user(update: Update, context: CallbackContext):
    if update.message.reply_to_message:
        user_id = update.message.reply_to_message.from_user.id
        try:
            context.bot.kick_chat_member(update.message.chat_id, user_id)
            update.message.reply_text("User has been banned.")
        except BadRequest as e:
            update.message.reply_text(f"Failed to ban user: {e}")
    else:
        update.message.reply_text("Reply to a user's message to ban them.")
    update.message.delete()

def mute_user(update: Update, context: CallbackContext):
    if update.message.reply_to_message:
        user_id = update.message.reply_to_message.from_user.id
        try:
            context.bot.restrict_chat_member(update.message.chat_id, user_id, permissions={"can_send_messages": False})
            update.message.reply_text("User has been muted.")
        except BadRequest as e:
            update.message.reply_text(f"Failed to mute user: {e}")
    else:
        update.message.reply_text("Reply to a user's message to mute them.")
    update.message.delete()

def unban_user(update: Update, context: CallbackContext):
    if len(context.args) == 1:
        user_id = int(context.args[0])
        try:
            context.bot.unban_chat_member(update.message.chat_id, user_id)
            update.message.reply_text(f"User {user_id} has been unbanned.")
        except BadRequest as e:
            update.message.reply_text(f"Failed to unban user: {e}")
    else:
        update.message.reply_text("Usage: /unban <user_id>")
    update.message.delete()

def unmute_user(update: Update, context: CallbackContext):
    if update.message.reply_to_message:
        user_id = update.message.reply_to_message.from_user.id
        try:
            context.bot.restrict_chat_member(update.message.chat_id, user_id, permissions={"can_send_messages": True})
            update.message.reply_text("User has been unmuted.")
        except BadRequest as e:
            update.message.reply_text(f"Failed to unmute user: {e}")
    else:
        update.message.reply_text("Reply to a user's message to unmute them.")
    update.message.delete()
